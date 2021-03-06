# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import event_pb2 as event__pb2


class EventStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.post_event = channel.unary_unary(
                '/Event/post_event',
                request_serializer=event__pb2.CreateEventRequest.SerializeToString,
                response_deserializer=event__pb2.CreateEventResponse.FromString,
                )


class EventServicer(object):
    """Missing associated documentation comment in .proto file."""

    def post_event(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'post_event': grpc.unary_unary_rpc_method_handler(
                    servicer.post_event,
                    request_deserializer=event__pb2.CreateEventRequest.FromString,
                    response_serializer=event__pb2.CreateEventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Event', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Event(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def post_event(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Event/post_event',
            event__pb2.CreateEventRequest.SerializeToString,
            event__pb2.CreateEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
