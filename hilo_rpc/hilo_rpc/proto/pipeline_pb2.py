# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hilo_rpc/proto/pipeline.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hilo_rpc.proto import metadata_pb2 as hilo__rpc_dot_proto_dot_metadata__pb2
from hilo_rpc.proto import sink_pb2 as hilo__rpc_dot_proto_dot_sink__pb2
from hilo_rpc.proto import source_pb2 as hilo__rpc_dot_proto_dot_source__pb2
from hilo_rpc.proto import stage_pb2 as hilo__rpc_dot_proto_dot_stage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hilo_rpc/proto/pipeline.proto',
  package='hilo_rpc.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1dhilo_rpc/proto/pipeline.proto\x12\x0ehilo_rpc.proto\x1a\x1dhilo_rpc/proto/metadata.proto\x1a\x19hilo_rpc/proto/sink.proto\x1a\x1bhilo_rpc/proto/source.proto\x1a\x1ahilo_rpc/proto/stage.proto\"\xfd\x07\n\x0ePipelineConfig\x12\x10\n\x08root_dir\x18\x01 \x01(\t\x12\x35\n\x06params\x18\x02 \x01(\x0b\x32%.hilo_rpc.proto.PipelineConfig.Params\x12\x35\n\x08metadata\x18\x03 \x01(\x0b\x32#.hilo_rpc.proto.MetadataStoreConfig\x12\x34\n\x06inputs\x18\x04 \x03(\x0b\x32$.hilo_rpc.proto.PipelineConfig.Input\x12\x36\n\x07outputs\x18\x05 \x03(\x0b\x32%.hilo_rpc.proto.PipelineConfig.Output\x12\x32\n\x05steps\x18\x06 \x03(\x0b\x32#.hilo_rpc.proto.PipelineConfig.Step\x1a\x1e\n\x06Params\x12\x14\n\x0c\x65nable_cache\x18\x01 \x01(\x08\x1a\xb2\x01\n\x0eSequenceConfig\x12\x34\n\x06inputs\x18\x01 \x03(\x0b\x32$.hilo_rpc.proto.PipelineConfig.Input\x12\x36\n\x07outputs\x18\x02 \x03(\x0b\x32%.hilo_rpc.proto.PipelineConfig.Output\x12\x32\n\x05steps\x18\x03 \x03(\x0b\x32#.hilo_rpc.proto.PipelineConfig.Step\x1aU\n\x08Sequence\x12\n\n\x02id\x18\x01 \x01(\t\x12=\n\x06\x63onfig\x18\x02 \x01(\x0b\x32-.hilo_rpc.proto.PipelineConfig.SequenceConfig\x1a\x8c\x01\n\x04Step\x12\x17\n\rsequence_path\x18\x01 \x01(\tH\x00\x12;\n\x08sequence\x18\x02 \x01(\x0b\x32\'.hilo_rpc.proto.PipelineConfig.SequenceH\x00\x12&\n\x05stage\x18\x03 \x01(\x0b\x32\x15.hilo_rpc.proto.StageH\x00\x42\x06\n\x04step\x1a\"\n\x07\x43hannel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x1au\n\x05Input\x12\x39\n\x07\x63hannel\x18\x01 \x01(\x0b\x32&.hilo_rpc.proto.PipelineConfig.ChannelH\x00\x12(\n\x06source\x18\x02 \x01(\x0b\x32\x16.hilo_rpc.proto.SourceH\x00\x42\x07\n\x05input\x1as\n\x06Output\x12\x39\n\x07\x63hannel\x18\x01 \x01(\x0b\x32&.hilo_rpc.proto.PipelineConfig.ChannelH\x00\x12$\n\x04sink\x18\x02 \x01(\x0b\x32\x14.hilo_rpc.proto.SinkH\x00\x42\x08\n\x06output\"x\n\x08Pipeline\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\t\x12.\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x1e.hilo_rpc.proto.PipelineConfig\"y\n\x15\x43reatePipelineRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12.\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x1e.hilo_rpc.proto.PipelineConfigb\x06proto3'
  ,
  dependencies=[hilo__rpc_dot_proto_dot_metadata__pb2.DESCRIPTOR,hilo__rpc_dot_proto_dot_sink__pb2.DESCRIPTOR,hilo__rpc_dot_proto_dot_source__pb2.DESCRIPTOR,hilo__rpc_dot_proto_dot_stage__pb2.DESCRIPTOR,])




_PIPELINECONFIG_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='hilo_rpc.proto.PipelineConfig.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_cache', full_name='hilo_rpc.proto.PipelineConfig.Params.enable_cache', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=473,
  serialized_end=503,
)

_PIPELINECONFIG_SEQUENCECONFIG = _descriptor.Descriptor(
  name='SequenceConfig',
  full_name='hilo_rpc.proto.PipelineConfig.SequenceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='hilo_rpc.proto.PipelineConfig.SequenceConfig.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='hilo_rpc.proto.PipelineConfig.SequenceConfig.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps', full_name='hilo_rpc.proto.PipelineConfig.SequenceConfig.steps', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=506,
  serialized_end=684,
)

_PIPELINECONFIG_SEQUENCE = _descriptor.Descriptor(
  name='Sequence',
  full_name='hilo_rpc.proto.PipelineConfig.Sequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hilo_rpc.proto.PipelineConfig.Sequence.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='hilo_rpc.proto.PipelineConfig.Sequence.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=686,
  serialized_end=771,
)

_PIPELINECONFIG_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='hilo_rpc.proto.PipelineConfig.Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_path', full_name='hilo_rpc.proto.PipelineConfig.Step.sequence_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='hilo_rpc.proto.PipelineConfig.Step.sequence', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage', full_name='hilo_rpc.proto.PipelineConfig.Step.stage', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='step', full_name='hilo_rpc.proto.PipelineConfig.Step.step',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=774,
  serialized_end=914,
)

_PIPELINECONFIG_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='hilo_rpc.proto.PipelineConfig.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hilo_rpc.proto.PipelineConfig.Channel.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='hilo_rpc.proto.PipelineConfig.Channel.url', index=1,
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
  serialized_start=916,
  serialized_end=950,
)

_PIPELINECONFIG_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='hilo_rpc.proto.PipelineConfig.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='hilo_rpc.proto.PipelineConfig.Input.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='hilo_rpc.proto.PipelineConfig.Input.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='input', full_name='hilo_rpc.proto.PipelineConfig.Input.input',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=952,
  serialized_end=1069,
)

_PIPELINECONFIG_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='hilo_rpc.proto.PipelineConfig.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='hilo_rpc.proto.PipelineConfig.Output.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sink', full_name='hilo_rpc.proto.PipelineConfig.Output.sink', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='output', full_name='hilo_rpc.proto.PipelineConfig.Output.output',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1071,
  serialized_end=1186,
)

_PIPELINECONFIG = _descriptor.Descriptor(
  name='PipelineConfig',
  full_name='hilo_rpc.proto.PipelineConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root_dir', full_name='hilo_rpc.proto.PipelineConfig.root_dir', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='hilo_rpc.proto.PipelineConfig.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='hilo_rpc.proto.PipelineConfig.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='hilo_rpc.proto.PipelineConfig.inputs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='hilo_rpc.proto.PipelineConfig.outputs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps', full_name='hilo_rpc.proto.PipelineConfig.steps', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PIPELINECONFIG_PARAMS, _PIPELINECONFIG_SEQUENCECONFIG, _PIPELINECONFIG_SEQUENCE, _PIPELINECONFIG_STEP, _PIPELINECONFIG_CHANNEL, _PIPELINECONFIG_INPUT, _PIPELINECONFIG_OUTPUT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=1186,
)


_PIPELINE = _descriptor.Descriptor(
  name='Pipeline',
  full_name='hilo_rpc.proto.Pipeline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hilo_rpc.proto.Pipeline.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='hilo_rpc.proto.Pipeline.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='hilo_rpc.proto.Pipeline.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='hilo_rpc.proto.Pipeline.owner', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='hilo_rpc.proto.Pipeline.config', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=1188,
  serialized_end=1308,
)


_CREATEPIPELINEREQUEST = _descriptor.Descriptor(
  name='CreatePipelineRequest',
  full_name='hilo_rpc.proto.CreatePipelineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hilo_rpc.proto.CreatePipelineRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='hilo_rpc.proto.CreatePipelineRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='hilo_rpc.proto.CreatePipelineRequest.owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='hilo_rpc.proto.CreatePipelineRequest.config', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1310,
  serialized_end=1431,
)

_PIPELINECONFIG_PARAMS.containing_type = _PIPELINECONFIG
_PIPELINECONFIG_SEQUENCECONFIG.fields_by_name['inputs'].message_type = _PIPELINECONFIG_INPUT
_PIPELINECONFIG_SEQUENCECONFIG.fields_by_name['outputs'].message_type = _PIPELINECONFIG_OUTPUT
_PIPELINECONFIG_SEQUENCECONFIG.fields_by_name['steps'].message_type = _PIPELINECONFIG_STEP
_PIPELINECONFIG_SEQUENCECONFIG.containing_type = _PIPELINECONFIG
_PIPELINECONFIG_SEQUENCE.fields_by_name['config'].message_type = _PIPELINECONFIG_SEQUENCECONFIG
_PIPELINECONFIG_SEQUENCE.containing_type = _PIPELINECONFIG
_PIPELINECONFIG_STEP.fields_by_name['sequence'].message_type = _PIPELINECONFIG_SEQUENCE
_PIPELINECONFIG_STEP.fields_by_name['stage'].message_type = hilo__rpc_dot_proto_dot_stage__pb2._STAGE
_PIPELINECONFIG_STEP.containing_type = _PIPELINECONFIG
_PIPELINECONFIG_STEP.oneofs_by_name['step'].fields.append(
  _PIPELINECONFIG_STEP.fields_by_name['sequence_path'])
_PIPELINECONFIG_STEP.fields_by_name['sequence_path'].containing_oneof = _PIPELINECONFIG_STEP.oneofs_by_name['step']
_PIPELINECONFIG_STEP.oneofs_by_name['step'].fields.append(
  _PIPELINECONFIG_STEP.fields_by_name['sequence'])
_PIPELINECONFIG_STEP.fields_by_name['sequence'].containing_oneof = _PIPELINECONFIG_STEP.oneofs_by_name['step']
_PIPELINECONFIG_STEP.oneofs_by_name['step'].fields.append(
  _PIPELINECONFIG_STEP.fields_by_name['stage'])
_PIPELINECONFIG_STEP.fields_by_name['stage'].containing_oneof = _PIPELINECONFIG_STEP.oneofs_by_name['step']
_PIPELINECONFIG_CHANNEL.containing_type = _PIPELINECONFIG
_PIPELINECONFIG_INPUT.fields_by_name['channel'].message_type = _PIPELINECONFIG_CHANNEL
_PIPELINECONFIG_INPUT.fields_by_name['source'].message_type = hilo__rpc_dot_proto_dot_source__pb2._SOURCE
_PIPELINECONFIG_INPUT.containing_type = _PIPELINECONFIG
_PIPELINECONFIG_INPUT.oneofs_by_name['input'].fields.append(
  _PIPELINECONFIG_INPUT.fields_by_name['channel'])
_PIPELINECONFIG_INPUT.fields_by_name['channel'].containing_oneof = _PIPELINECONFIG_INPUT.oneofs_by_name['input']
_PIPELINECONFIG_INPUT.oneofs_by_name['input'].fields.append(
  _PIPELINECONFIG_INPUT.fields_by_name['source'])
_PIPELINECONFIG_INPUT.fields_by_name['source'].containing_oneof = _PIPELINECONFIG_INPUT.oneofs_by_name['input']
_PIPELINECONFIG_OUTPUT.fields_by_name['channel'].message_type = _PIPELINECONFIG_CHANNEL
_PIPELINECONFIG_OUTPUT.fields_by_name['sink'].message_type = hilo__rpc_dot_proto_dot_sink__pb2._SINK
_PIPELINECONFIG_OUTPUT.containing_type = _PIPELINECONFIG
_PIPELINECONFIG_OUTPUT.oneofs_by_name['output'].fields.append(
  _PIPELINECONFIG_OUTPUT.fields_by_name['channel'])
_PIPELINECONFIG_OUTPUT.fields_by_name['channel'].containing_oneof = _PIPELINECONFIG_OUTPUT.oneofs_by_name['output']
_PIPELINECONFIG_OUTPUT.oneofs_by_name['output'].fields.append(
  _PIPELINECONFIG_OUTPUT.fields_by_name['sink'])
_PIPELINECONFIG_OUTPUT.fields_by_name['sink'].containing_oneof = _PIPELINECONFIG_OUTPUT.oneofs_by_name['output']
_PIPELINECONFIG.fields_by_name['params'].message_type = _PIPELINECONFIG_PARAMS
_PIPELINECONFIG.fields_by_name['metadata'].message_type = hilo__rpc_dot_proto_dot_metadata__pb2._METADATASTORECONFIG
_PIPELINECONFIG.fields_by_name['inputs'].message_type = _PIPELINECONFIG_INPUT
_PIPELINECONFIG.fields_by_name['outputs'].message_type = _PIPELINECONFIG_OUTPUT
_PIPELINECONFIG.fields_by_name['steps'].message_type = _PIPELINECONFIG_STEP
_PIPELINE.fields_by_name['config'].message_type = _PIPELINECONFIG
_CREATEPIPELINEREQUEST.fields_by_name['config'].message_type = _PIPELINECONFIG
DESCRIPTOR.message_types_by_name['PipelineConfig'] = _PIPELINECONFIG
DESCRIPTOR.message_types_by_name['Pipeline'] = _PIPELINE
DESCRIPTOR.message_types_by_name['CreatePipelineRequest'] = _CREATEPIPELINEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PipelineConfig = _reflection.GeneratedProtocolMessageType('PipelineConfig', (_message.Message,), {

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINECONFIG_PARAMS,
    '__module__' : 'hilo_rpc.proto.pipeline_pb2'
    # @@protoc_insertion_point(class_scope:hilo_rpc.proto.PipelineConfig.Params)
    })
  ,

  'SequenceConfig' : _reflection.GeneratedProtocolMessageType('SequenceConfig', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINECONFIG_SEQUENCECONFIG,
    '__module__' : 'hilo_rpc.proto.pipeline_pb2'
    # @@protoc_insertion_point(class_scope:hilo_rpc.proto.PipelineConfig.SequenceConfig)
    })
  ,

  'Sequence' : _reflection.GeneratedProtocolMessageType('Sequence', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINECONFIG_SEQUENCE,
    '__module__' : 'hilo_rpc.proto.pipeline_pb2'
    # @@protoc_insertion_point(class_scope:hilo_rpc.proto.PipelineConfig.Sequence)
    })
  ,

  'Step' : _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINECONFIG_STEP,
    '__module__' : 'hilo_rpc.proto.pipeline_pb2'
    # @@protoc_insertion_point(class_scope:hilo_rpc.proto.PipelineConfig.Step)
    })
  ,

  'Channel' : _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINECONFIG_CHANNEL,
    '__module__' : 'hilo_rpc.proto.pipeline_pb2'
    # @@protoc_insertion_point(class_scope:hilo_rpc.proto.PipelineConfig.Channel)
    })
  ,

  'Input' : _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINECONFIG_INPUT,
    '__module__' : 'hilo_rpc.proto.pipeline_pb2'
    # @@protoc_insertion_point(class_scope:hilo_rpc.proto.PipelineConfig.Input)
    })
  ,

  'Output' : _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINECONFIG_OUTPUT,
    '__module__' : 'hilo_rpc.proto.pipeline_pb2'
    # @@protoc_insertion_point(class_scope:hilo_rpc.proto.PipelineConfig.Output)
    })
  ,
  'DESCRIPTOR' : _PIPELINECONFIG,
  '__module__' : 'hilo_rpc.proto.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.PipelineConfig)
  })
_sym_db.RegisterMessage(PipelineConfig)
_sym_db.RegisterMessage(PipelineConfig.Params)
_sym_db.RegisterMessage(PipelineConfig.SequenceConfig)
_sym_db.RegisterMessage(PipelineConfig.Sequence)
_sym_db.RegisterMessage(PipelineConfig.Step)
_sym_db.RegisterMessage(PipelineConfig.Channel)
_sym_db.RegisterMessage(PipelineConfig.Input)
_sym_db.RegisterMessage(PipelineConfig.Output)

Pipeline = _reflection.GeneratedProtocolMessageType('Pipeline', (_message.Message,), {
  'DESCRIPTOR' : _PIPELINE,
  '__module__' : 'hilo_rpc.proto.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.Pipeline)
  })
_sym_db.RegisterMessage(Pipeline)

CreatePipelineRequest = _reflection.GeneratedProtocolMessageType('CreatePipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPIPELINEREQUEST,
  '__module__' : 'hilo_rpc.proto.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:hilo_rpc.proto.CreatePipelineRequest)
  })
_sym_db.RegisterMessage(CreatePipelineRequest)


# @@protoc_insertion_point(module_scope)
