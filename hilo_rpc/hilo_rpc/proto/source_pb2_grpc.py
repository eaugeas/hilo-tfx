# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from hilo_rpc.proto import source_pb2 as hilo__rpc_dot_proto_dot_source__pb2


class SourceApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateSource = channel.unary_unary(
        '/hilo_rpc.proto.SourceApi/CreateSource',
        request_serializer=hilo__rpc_dot_proto_dot_source__pb2.CreateSourceRequest.SerializeToString,
        response_deserializer=hilo__rpc_dot_proto_dot_source__pb2.CreateSourceResponse.FromString,
        )
    self.DeleteSource = channel.unary_unary(
        '/hilo_rpc.proto.SourceApi/DeleteSource',
        request_serializer=hilo__rpc_dot_proto_dot_source__pb2.DeleteSourceRequest.SerializeToString,
        response_deserializer=hilo__rpc_dot_proto_dot_source__pb2.DeleteSourceResponse.FromString,
        )
    self.GetSource = channel.unary_unary(
        '/hilo_rpc.proto.SourceApi/GetSource',
        request_serializer=hilo__rpc_dot_proto_dot_source__pb2.GetSourceRequest.SerializeToString,
        response_deserializer=hilo__rpc_dot_proto_dot_source__pb2.GetSourceResponse.FromString,
        )


class SourceApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateSource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SourceApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateSource': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSource,
          request_deserializer=hilo__rpc_dot_proto_dot_source__pb2.CreateSourceRequest.FromString,
          response_serializer=hilo__rpc_dot_proto_dot_source__pb2.CreateSourceResponse.SerializeToString,
      ),
      'DeleteSource': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSource,
          request_deserializer=hilo__rpc_dot_proto_dot_source__pb2.DeleteSourceRequest.FromString,
          response_serializer=hilo__rpc_dot_proto_dot_source__pb2.DeleteSourceResponse.SerializeToString,
      ),
      'GetSource': grpc.unary_unary_rpc_method_handler(
          servicer.GetSource,
          request_deserializer=hilo__rpc_dot_proto_dot_source__pb2.GetSourceRequest.FromString,
          response_serializer=hilo__rpc_dot_proto_dot_source__pb2.GetSourceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hilo_rpc.proto.SourceApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
