from functools import reduce
from typing import Any, Callable, Dict, List, Optional, Text, Type, Union

from google.protobuf.message import Message
from google.protobuf.descriptor import Descriptor
from google.protobuf.pyext._message import (ScalarMapContainer,
                                            MessageMapContainer,
                                            RepeatedScalarContainer,
                                            RepeatedCompositeContainer)

from hilo_rpc.serialize.symbol_loader import ProtobufSymbolLoader

_SYMBOL_LOADER = ProtobufSymbolLoader()


def camel_case_to_snake_case(s: Text) -> Text:
    """camel_case_to_snake_case converts the formatting in
    s from camelCase to snake_case"""
    return reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, s).lower()


def _get_message_instance(message: Optional[Union[Type[Message],
                                                  Message]] = None,
                          url: Optional[Text] = None) -> Message:
    if message:
        if isinstance(message, Message):
            record: Message = message
        else:
            record: Message = message()
    elif url:
        record: Message = _SYMBOL_LOADER.load(url)()
    else:
        raise ValueError('either `message` or `url` must be set')
    return record


class _Value:
    def typedef(
            self,
            serializer: '_Serializer',
            value: Any,
            descriptor: Descriptor,
    ) -> Any:
        raise NotImplementedError()

    def serialize(
            self,
            serializer: '_Serializer',
            value: Any,
    ) -> Any:
        raise NotImplementedError()

    def deserialize(
            self,
            serializer: '_Serializer',
            value: Any,
            r: Any,
            descriptor: Descriptor,
    ) -> Any:
        raise NotImplementedError()


class _CompositeValue(_Value):
    def __init__(self, typedef: Callable[['_Serializer', Any, Descriptor],
                                         Any],
                 serializer: Callable[['_Serializer', Any], Any],
                 deserializer: Callable[['_Serializer', Any, Any, Descriptor],
                                        Any]):
        self._typedef = typedef
        self._serializer = serializer
        self._deserializer = deserializer

    def typedef(self, serializer: '_Serializer', value: Any,
                descriptor: Descriptor) -> Any:
        return self._typedef(serializer, value, descriptor)

    def serialize(self, serializer: '_Serializer', value: Any) -> Any:
        return self._serializer(serializer, value)

    def deserialize(self, serializer: '_Serializer', value: Any, r: Any,
                    descriptor: Descriptor) -> Any:
        return self._deserializer(serializer, value, r, descriptor)


class _Serializer:
    def __init__(self):
        self._urls = {}

    def add_url(self, url: Text):
        self._urls[url] = True

    def is_deserialized(self, url: Text) -> bool:
        return url in self._urls

    def typedef(self, value: Any, descriptor: Descriptor) -> Any:
        t = _Serializer._value(value, _Types.simple_types)
        if t is not None:
            return t.typedef(self, value, descriptor)

        t = _Serializer._value(value, _Types.composite_types)
        if t is not None:
            return t.typedef(self, value, descriptor)

        raise ValueError(
            'Do not know how to serialize value {0}'.format(value))

    def serialize(self, value: Any) -> Any:
        t = _Serializer._value(value, _Types.simple_types)
        if t is not None:
            return t.serialize(self, value)

        t = _Serializer._value(value, _Types.composite_types)
        if t is not None:
            return t.serialize(self, value)

        raise ValueError(
            'Do not know how to serialize value {0}'.format(value))

    def deserialize(self, value: Any, r: Any, descriptor: Descriptor) -> Any:
        t = _Serializer._value(value, _Types.simple_types)
        if t is not None:
            return t.deserialize(self, value, r, descriptor)

        t = _Serializer._value(value, _Types.composite_types)
        if t is not None:
            return t.deserialize(self, value, r, descriptor)

        raise ValueError(
            'Do not know how to deserialize value {0}'.format(value))

    @staticmethod
    def _get_type_from_typedef(value: Any, typedef: '_TypeDef') -> Any:
        types = filter(
            lambda tp: isinstance(value, tp),
            typedef.keys(),
        )

        for t in types:
            return typedef[t].typedef

        raise ValueError('Unknown type instance for value {0}'.format(value))

    @staticmethod
    def get_type_from_simple_value(value: Any) -> Any:
        return _Serializer._get_type_from_typedef(value, _Types.simple_types)

    @staticmethod
    def get_type_from_composite_value(value: Any) -> Any:
        return _Serializer._get_type_from_typedef(value,
                                                  _Types.composite_types)

    @staticmethod
    def get_type_from_value(value: Any) -> Any:
        if _Serializer.is_simple(value):
            _Serializer.get_type_from_simple_value(value)
        elif _Serializer.is_composite(value):
            _Serializer.get_type_from_composite_value(value)
        else:
            raise ValueError(
                'Unknown type instance for value {0}'.format(value))

    @staticmethod
    def _value(value: Any, typedef: '_TypeDef') -> Optional[_Value]:
        types = filter(
            lambda tp: isinstance(value, tp),
            typedef.keys(),
        )

        for t in types:
            return typedef[t]

        return None

    @staticmethod
    def simple_value(value: Any) -> '_SimpleValue':
        t = _Serializer._value(value, _Types.simple_types)
        if t is None:
            raise ValueError('Value {0} is not a simple value'.format(value))
        else:
            if not isinstance(t, _SimpleValue):
                raise RuntimeError(
                    'All elements in _Types.simple_types must be '
                    'an instance of _SimpleValue')
            return t

    @staticmethod
    def composite_value(value: Any) -> _CompositeValue:
        t = _Serializer._value(value, _Types.composite_types)
        if t is None:
            raise ValueError('Value {0} is not a simple value'.format(value))
        else:
            if not isinstance(t, _CompositeValue):
                raise RuntimeError(
                    'All elements in _Types.composite_types must be '
                    'an instance of _CompositeValue')

            return t

    @staticmethod
    def is_simple(value: Any) -> bool:
        """is_simple returns true if the value is a simple builtin type.
        """
        return _Serializer._value(value, _Types.simple_types) is not None

    @staticmethod
    def is_composite(value: Any) -> bool:
        """is_composite returns true if the value is a protobuf
        composite type
        """
        return _Serializer._value(value, _Types.composite_types) is not None

    @staticmethod
    def is_valid(value: Any) -> bool:
        return _Serializer.is_simple(value) or _Serializer.is_composite(value)

    @staticmethod
    def is_not_simple(value: Any) -> bool:
        return not _Serializer.is_simple(value)


class _MessageMapContainer(object):
    @staticmethod
    def typedef(
            serializer: _Serializer,
            value: MessageMapContainer,
            descriptor: Descriptor,
    ) -> Dict[Any, Any]:
        results: Dict[Any, Any] = {}
        symbol = _SYMBOL_LOADER.load(descriptor.message_type.full_name)
        results['entry'] = serializer.typedef(symbol(), descriptor)
        return results

    @staticmethod
    def serialize(
            serializer: _Serializer,
            value: MessageMapContainer,
    ) -> Dict[Any, Any]:
        results: Dict[Any, Any] = {}
        for key in value:
            s_key = serializer.serialize(key)
            s_value = serializer.serialize(value[key])
            results[s_key] = s_value
        return results

    @staticmethod
    def deserialize(serializer: _Serializer, value: MessageMapContainer,
                    collection: Dict[Any, Any],
                    descriptor: Descriptor) -> MessageMapContainer:
        for key in collection:
            entry = value.get_or_create(key)
            serializer.deserialize(entry, collection[key], entry.DESCRIPTOR)
        return value


class _ScalarMapContainer(object):
    @staticmethod
    def typedef(serializer: _Serializer, value: ScalarMapContainer,
                descriptor: Descriptor) -> Dict[Any, Any]:
        for key, v in zip(_Types.simple_types, _Types.simple_types):
            try:
                e_key = _Types.simple_types[key].example()
                e_value = _Types.simple_types[v].example()
                value[e_key] = e_value
                del value[e_key]

                t_key = _Types.simple_types[key].typedef(
                    serializer, e_key, descriptor)
                t_value = _Types.simple_types[v].typedef(
                    serializer, e_value, descriptor)
                return {t_key: t_value}
            except TypeError:
                pass
        raise ValueError(
            'Unknown ScalarMapContainer subtype for {0}'.format(value))

    @staticmethod
    def serialize(
            serializer: _Serializer,
            value: ScalarMapContainer,
    ) -> Dict[Any, Any]:
        result: Dict[Any, Any] = {}
        for key in value:
            result[key] = value[key]
        return result

    @staticmethod
    def deserialize(
            serializer: _Serializer,
            value: ScalarMapContainer,
            collection: Dict[Any, Any],
            descriptor: Descriptor,
    ) -> ScalarMapContainer:
        for key in collection:
            value[key] = collection[key]
        return value


class _RepeatedCompositeContainer(object):
    @staticmethod
    def typedef(
            serializer: _Serializer,
            value: RepeatedScalarContainer,
            descriptor: Descriptor,
    ) -> List[Any]:
        results: List[Any] = []
        symbol = _SYMBOL_LOADER.load(descriptor.message_type.full_name)
        results.append(serializer.typedef(symbol(), descriptor))
        return results

    @staticmethod
    def serialize(
            serializer: _Serializer,
            value: RepeatedScalarContainer,
    ) -> List[Any]:
        results: List[Any] = []
        for v in value:
            results.append(serializer.serialize(v))
        return results

    @staticmethod
    def deserialize(
        serializer: _Serializer,
        value: RepeatedScalarContainer,
        collection: List[Any],
        descriptor: Descriptor,
    ):
        for v in collection:
            symbol = _SYMBOL_LOADER.load(descriptor.message_type.full_name)
            value.append(serializer.deserialize(symbol(), v, descriptor))
        return value


class _RepeatedScalarContainer(object):
    @staticmethod
    def typedef(
            serializer: _Serializer,
            value: RepeatedScalarContainer,
            descriptor: Descriptor,
    ) -> List[Any]:
        for t in _Types.simple_types:
            try:
                example = _Types.simple_types[t].example()
                value.append(example)
                value.pop()
                return [
                    _Types.simple_types[t].typedef(serializer, example,
                                                   descriptor)
                ]
            except TypeError:
                pass
        raise ValueError(
            'Unknown RepeatedScalarContainer subtype for {0}'.format(value))

    @staticmethod
    def serialize(
            serializer: _Serializer,
            value: RepeatedScalarContainer,
    ) -> List[Any]:
        result: List[Any] = []
        for v in value:
            result.append(v)
        return result

    @staticmethod
    def deserialize(serializer: _Serializer, value: RepeatedScalarContainer,
                    collection: List[Any],
                    descriptor: Descriptor) -> RepeatedScalarContainer:
        for v in collection:
            value.append(v)
        return value


class _Message(object):
    @staticmethod
    def typedef(
            serializer: _Serializer,
            value: Message,
            descriptor: Descriptor,
    ) -> Dict[Text, Any]:

        serializer.add_url(descriptor.full_name)
        result: Dict[Text, Any] = {}
        for d_field in value.DESCRIPTOR.fields:
            field = getattr(value, d_field.name)

            if (serializer.is_deserialized(d_field.full_name)
                    and isinstance(field, Message)):
                result[d_field.name] = d_field.full_name
            else:
                serializer.add_url(d_field.full_name)
                result[d_field.name] = serializer.typedef(field, d_field)
        return result

    @staticmethod
    def _is_oneof(value: Any) -> bool:
        if not isinstance(value, Message):
            return False
        for field in value.DESCRIPTOR.fields:
            return field.containing_oneof is not None
        return False

    @staticmethod
    def _oneof_name(value: Any) -> Text:
        if not isinstance(value, Message):
            raise ValueError(
                'Not a oneof instance. Received {0}'.format(value))
        for field in value.DESCRIPTOR.fields:
            if field.containing_oneof is not None:
                return field.containing_oneof.name
            raise ValueError(
                'Not a oneof instance. Received {0}'.format(value))

    @staticmethod
    def serialize(serializer: _Serializer, value: Message) -> Dict[Text, Any]:
        result: Dict[Text, Any] = {}
        descriptor = value.DESCRIPTOR

        for d_field in descriptor.fields:
            field = getattr(value, d_field.name)
            result[d_field.name] = serializer.serialize(field)

            if _Message._is_oneof(field):
                oneof_name = _Message._oneof_name(field)
                oneof_prop_name = field.WhichOneof(oneof_name)
                if oneof_prop_name is not None:
                    result[d_field.name] = {
                        oneof_prop_name:
                        serializer.serialize(getattr(field, oneof_prop_name))
                    }
            else:
                result[d_field.name] = serializer.serialize(field)
        return result

    @staticmethod
    def deserialize(
            serializer: _Serializer,
            value: Message,
            collection: Dict[Text, Any],
            descriptor: Descriptor,
    ) -> Message:
        descriptor = value.DESCRIPTOR
        for d_field in descriptor.fields:
            if d_field.name not in collection:
                continue

            attribute = getattr(value, d_field.name)
            deserialized = serializer.deserialize(attribute,
                                                  collection[d_field.name],
                                                  d_field)

            if serializer.is_simple(attribute):
                setattr(value, d_field.name, deserialized)

        return value


class _SimpleValue(_Value):
    def __init__(
        self,
        typedef: Text,
        example: Any,
        t: Type,
    ):
        self._typedef = typedef
        self._example = example
        self._t = t

    def typecheck(self, value: Any):
        if not isinstance(value, self._t):
            try:
                self._t(value)
                return
            except TypeError:
                pass
            raise ValueError('Expected {0} type. Received {1}'.format(
                self._typedef, value))

    def typedef(self, serializer: _Serializer, value: Any,
                descriptor: Descriptor) -> Text:
        self.typecheck(value)
        return self._typedef

    def example(self) -> Any:
        return self._example

    def serialize(self, serializer: _Serializer, value: Any) -> Any:
        self.typecheck(value)
        return self._t(value)

    def deserialize(self, serializer: _Serializer, value: Any, r: Any,
                    descriptor: Descriptor) -> Any:
        self.typecheck(value)
        self.typecheck(r)
        if r is None:
            return self._t()
        return self._t(r)


_CompositeTypeDef = Dict[Type, _CompositeValue]
_SimpleTypeDef = Dict[Type, _SimpleValue]
_TypeDef = Union[_SimpleTypeDef, _CompositeTypeDef]


class _Types(object):
    composite_types: _CompositeTypeDef = {
        ScalarMapContainer:
        _CompositeValue(_ScalarMapContainer.typedef,
                        _ScalarMapContainer.serialize,
                        _ScalarMapContainer.deserialize),
        MessageMapContainer:
        _CompositeValue(_MessageMapContainer.typedef,
                        _MessageMapContainer.serialize,
                        _MessageMapContainer.deserialize),
        RepeatedScalarContainer:
        _CompositeValue(_RepeatedScalarContainer.typedef,
                        _RepeatedScalarContainer.serialize,
                        _RepeatedScalarContainer.deserialize),
        RepeatedCompositeContainer:
        _CompositeValue(_RepeatedCompositeContainer.typedef,
                        _RepeatedCompositeContainer.serialize,
                        _RepeatedCompositeContainer.deserialize),
        Message:
        _CompositeValue(_Message.typedef, _Message.serialize,
                        _Message.deserialize)
    }

    simple_types: _SimpleTypeDef = {
        bool: _SimpleValue('bool', True, bool),
        str: _SimpleValue('str', 'str', str),
        bytes: _SimpleValue('bytes', b'bytes', bytes),
        int: _SimpleValue('int', 1, int),
        float: _SimpleValue('float', 1.1, float),
    }


def _namespace(current: Text, addition: Text, sep: Text = '.') -> Text:
    if current:
        return sep.join([current, addition])
    else:
        return addition


def _flatten_dict_rec(namespace: Text, d: Dict[str, Any], result: Dict[str,
                                                                       Any]):
    for key in d:
        key_namespace = _namespace(namespace, key)
        if isinstance(d[key], int):
            result[key_namespace] = d[key]
        elif isinstance(d[key], float):
            result[key_namespace] = d[key]
        elif isinstance(d[key], str):
            result[key_namespace] = d[key]
        elif isinstance(d[key], dict):
            _flatten_dict_rec(key_namespace, d[key], result)
        elif isinstance(d[key], list):
            for i in range(0, len(d[key])):
                el_namespace = _namespace(key_namespace, str(i))
                _flatten_dict_rec(el_namespace, d[key][i], result)
        else:
            raise ValueError('Unexpected type for value {0}'.format(d[key]))


def flatten(d: Dict[str, Any], namespace: Text = '') -> Dict[str, Any]:
    """flatten flattens a multi-level dictionary into a single level
    dictionary.

    For example:
        d = {'key1': {'key2': 'value1'}}
     would be serialized into
        d = {'key1.key2': 'value1'}

    The input dictionary's values are expected to be simple values
    such as int, float, str, or other dictionaries or lists

    :param d: the dictionary to flatten
    :param namespace: a namespace that may be added to every key
    :return: a flattened dictionary
    """
    result: Dict[str, Any] = {}
    _flatten_dict_rec(namespace, d, result)
    return result


def unflatten(d: Dict[str, Any], namespace: Text = '') -> Dict[str, Any]:
    """
    unflatten is the opposite operation of flatten. It takes
    a single level dictionary and unflattens it to a multi level dictionary.

    For example:
        d = {'key1.key2': 'value1'}
     would be unflattened  into
        d = {'key1': {'key2': 'value1'}}

    :param d: dictionary to flatten
    :param namespace: whether to strip a namespace from the dictionary keys
    :return: a flattened dictionary
    """
    result = {}

    for key in d:
        newkey = key
        if namespace and key.startswith(namespace + '.'):
            newkey = key.lstrip(namespace)[1:]

        if isinstance(d[key], dict):
            raise ValueError('unflatten_dict expects a '
                             'single level dictionary. Received {0}'.format(d))
        split = newkey.split('.')
        it_result = result
        for level in split[:-1]:
            if level not in it_result:
                it_result[level] = {}
            it_result = it_result[level]
        it_result[split[-1]] = d[key]

    return result


def typedef(message: Union[Type[Message], Message]) -> Dict[str, Any]:
    """typedef serializes the message type into a dictionary of its types
    instead of serializing the values. For serializing the values
    look at serialize.

    :param message: a protobuf message instance or a class from which an
    instance can be created
    :return: a serialization of the message as a dictionary
    """
    if not isinstance(message, Message):
        message = message()
    serializer = _Serializer()
    return serializer.typedef(message, message.DESCRIPTOR)


def serialize(message: Union[Type[Message], Message]) -> Dict[str, Any]:
    """serialize_to_dict serializes the message type
    into a dictionary.

    :param message: a protobuf message instance or a class from which an
    instance can be created
    :return: a serialization of the message as a dictionary
    """
    if not isinstance(message, Message):
        message = message()
    serializer = _Serializer()
    return serializer.serialize(message)


def deserialize(d: Dict[Text, Any],
                message: Optional[Union[Type[Message], Message]] = None,
                url: Optional[Text] = None) -> Message:
    """deserialize the contents of the dictionary into a message of
    the provided type

    :param d: the dictionary with the contents to be deserialized
    :param message: either a message type or the message instance where
    the contents will be put
    :param url: url to the message that the symbol loader can use to
    load a new instance of the message
    :return: an instance of message with the contents of d
    """
    message: Message = _get_message_instance(message=message, url=url)
    serializer = _Serializer()
    return serializer.deserialize(message, d, message.DESCRIPTOR)
