import logging
from concurrent import futures

import event_pb2
import event_pb2_grpc
import grpc
from producer import send_event
from settings import grpc_settings


class Event(event_pb2_grpc.EventServicer):
    def post_event(self, request, context):
        send_event(request.message)
        return event_pb2.CreateEventResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    event_pb2_grpc.add_EventServicer_to_server(Event(), server)
    server.add_insecure_port(grpc_settings.url)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
