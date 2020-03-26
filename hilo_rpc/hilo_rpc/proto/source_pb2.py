# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hilo_rpc/proto/source.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from hilo_rpc.proto import storage_pb2 as hilo__rpc_dot_proto_dot_storage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hilo_rpc/proto/source.proto',
  package='hilo_rpc.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1bhilo_rpc/proto/source.proto\x12\x0ehilo_rpc.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1chilo_rpc/proto/storage.proto\"\xc4\x01\n\x06Source\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x06\x63onfig\x18\x06 \x01(\x0b\x32\x1b.hilo_rpc.proto.InputConfig\"8\n\x13\x43reateSourceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\"\n\x14\x43reateSourceResponse\x12\n\n\x02id\x18\x01 \x01(\t\"!\n\x13\x44\x65leteSourceRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x16\n\x14\x44\x65leteSourceResponse\"\x1e\n\x10GetSourceRequest\x12\n\n\x02id\x18\x01 \x01(\t\";\n\x11GetSourceResponse\x12&\n\x06source\x18\x01 \x01(\x0b\x32\x16.hilo_rpc.proto.Source2\x93\x02\n\tSourceApi\x12Y\n\x0c\x43reateSource\x12#.hilo_rpc.proto.CreateSourceRequest\x1a$.hilo_rpc.proto.CreateSourceResponse\x12Y\n\x0c\x44\x65leteSource\x12#.hilo_rpc.proto.DeleteSourceRequest\x1a$.hilo_rpc.proto.DeleteSourceResponse\x12P\n\tGetSource\x12 .hilo_rpc.proto.GetSourceRequest\x1a!.hilo_rpc.proto.GetSourceResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,hilo__rpc_dot_proto_dot_storage__pb2.DESCRIPTOR,])




_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='hilo_rpc.proto.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hilo_rpc.proto.Source.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='hilo_rpc.proto.Source.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='hilo_rpc.proto.Source.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='hilo_rpc.proto.Source.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='hilo_rpc.proto.Source.updated_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='hilo_rpc.proto.Source.config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=307,
)


_CREATESOURCEREQUEST = _descriptor.Descriptor(
  name='CreateSourceRequest',
  full_name='hilo_rpc.proto.CreateSourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hilo_rpc.proto.CreateSourceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='hilo_rpc.proto.CreateSourceRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=365,
)


_CREATESOURCERESPONSE = _descriptor.Descriptor(
  name='CreateSourceResponse',
  full_name='hilo_rpc.proto.CreateSourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hilo_rpc.proto.CreateSourceResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=401,
)


_DELETESOURCEREQUEST = _descriptor.Descriptor(
  name='DeleteSourceRequest',
  full_name='hilo_rpc.proto.DeleteSourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hilo_rpc.proto.DeleteSourceRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=436,
)


_DELETESOURCERESPONSE = _descriptor.Descriptor(
  name='DeleteSourceResponse',
  full_name='hilo_rpc.proto.DeleteSourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=460,
)


_GETSOURCEREQUEST = _descriptor.Descriptor(
  name='GetSourceRequest',
  full_name='hilo_rpc.proto.GetSourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hilo_rpc.proto.GetSourceRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=462,
  serialized_end=492,
)


_GETSOURCERESPONSE = _descriptor.Descriptor(
  name='GetSourceResponse',
  full_name='hilo_rpc.proto.GetSourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='hilo_rpc.proto.GetSourceResponse.source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=494,
  serialized_end=553,
)

_SOURCE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SOURCE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SOURCE.fields_by_name['config'].message_type = hilo__rpc_dot_proto_dot_storage__pb2._INPUTCONFIG
_GETSOURCERESPONSE.fields_by_name['source'].message_type = _SOURCE
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['CreateSourceRequest'] = _CREATESOURCEREQUEST
DESCRIPTOR.message_types_by_name['CreateSourceResponse'] = _CREATESOURCERESPONSE
DESCRIPTOR.message_types_by_name['DeleteSourceRequest'] = _DELETESOURCEREQUEST
DESCRIPTOR.message_types_by_name['DeleteSourceResponse'] = _DELETESOURCERESPONSE
DESCRIPTOR.message_types_by_name['GetSourceRequest'] = _GETSOURCEREQUEST
DESCRIPTOR.message_types_by_name['GetSourceResponse'] = _GETSOURCERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'hilo_rpc.proto.source_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.Source)
  })
_sym_db.RegisterMessage(Source)

CreateSourceRequest = _reflection.GeneratedProtocolMessageType('CreateSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESOURCEREQUEST,
  '__module__' : 'hilo_rpc.proto.source_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.CreateSourceRequest)
  })
_sym_db.RegisterMessage(CreateSourceRequest)

CreateSourceResponse = _reflection.GeneratedProtocolMessageType('CreateSourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESOURCERESPONSE,
  '__module__' : 'hilo_rpc.proto.source_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.CreateSourceResponse)
  })
_sym_db.RegisterMessage(CreateSourceResponse)

DeleteSourceRequest = _reflection.GeneratedProtocolMessageType('DeleteSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESOURCEREQUEST,
  '__module__' : 'hilo_rpc.proto.source_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.DeleteSourceRequest)
  })
_sym_db.RegisterMessage(DeleteSourceRequest)

DeleteSourceResponse = _reflection.GeneratedProtocolMessageType('DeleteSourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETESOURCERESPONSE,
  '__module__' : 'hilo_rpc.proto.source_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.DeleteSourceResponse)
  })
_sym_db.RegisterMessage(DeleteSourceResponse)

GetSourceRequest = _reflection.GeneratedProtocolMessageType('GetSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSOURCEREQUEST,
  '__module__' : 'hilo_rpc.proto.source_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.GetSourceRequest)
  })
_sym_db.RegisterMessage(GetSourceRequest)

GetSourceResponse = _reflection.GeneratedProtocolMessageType('GetSourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSOURCERESPONSE,
  '__module__' : 'hilo_rpc.proto.source_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.GetSourceResponse)
  })
_sym_db.RegisterMessage(GetSourceResponse)



_SOURCEAPI = _descriptor.ServiceDescriptor(
  name='SourceApi',
  full_name='hilo_rpc.proto.SourceApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=556,
  serialized_end=831,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateSource',
    full_name='hilo_rpc.proto.SourceApi.CreateSource',
    index=0,
    containing_service=None,
    input_type=_CREATESOURCEREQUEST,
    output_type=_CREATESOURCERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSource',
    full_name='hilo_rpc.proto.SourceApi.DeleteSource',
    index=1,
    containing_service=None,
    input_type=_DELETESOURCEREQUEST,
    output_type=_DELETESOURCERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSource',
    full_name='hilo_rpc.proto.SourceApi.GetSource',
    index=2,
    containing_service=None,
    input_type=_GETSOURCEREQUEST,
    output_type=_GETSOURCERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SOURCEAPI)

DESCRIPTOR.services_by_name['SourceApi'] = _SOURCEAPI

# @@protoc_insertion_point(module_scope)
