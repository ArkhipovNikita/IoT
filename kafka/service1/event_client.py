from __future__ import print_function

import logging

import grpc
import event_pb2
import event_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = event_pb2_grpc.EventStub(channel)

        # UNARY CALL
        response = stub.post_event(event_pb2.CreateEventRequest(message='test'))
        print('Ok')


if __name__ == '__main__':
    logging.basicConfig()
    run()
