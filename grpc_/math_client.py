from __future__ import print_function

import logging

import grpc
import math_pb2
import math_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = math_pb2_grpc.MathStub(channel)

        # UNARY CALL
        response = stub.get_sqrt(math_pb2.SqrtRequest(number=4))
        print("Math client received (sqrt): " + str(response.sqrt))

        # CLIENT STREAMING
        data = [
            math_pb2.SqrtRequest(number=3),
            math_pb2.SqrtRequest(number=1),
            math_pb2.SqrtRequest(number=4),
            math_pb2.SqrtRequest(number=6),
            math_pb2.SqrtRequest(number=-1),
        ]
        response = stub.get_std(iter(data))
        print("Math client received (std): " + str(response.std))

        # SERVER STREAMING
        responses = stub.get_multipliers(math_pb2.MultipliersRequest(number=114))
        print("Math client received (multipliers): " +
              ' * '.join(map(lambda r: str(r.number), responses)))

        # BIDIRECTIONAL STREAMING
        data = [
            math_pb2.MaxRequest(number=3),
            math_pb2.MaxRequest(number=1),
            math_pb2.MaxRequest(number=4),
            math_pb2.MaxRequest(number=6),
            math_pb2.MaxRequest(number=-1),
        ]
        responses = stub.get_max(iter(data))
        print("Math client received (max): " +
              ', '.join(map(lambda r: str(r.max), responses)))


if __name__ == '__main__':
    logging.basicConfig()
    run()
