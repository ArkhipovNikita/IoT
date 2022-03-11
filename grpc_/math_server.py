import logging
import math
import statistics
from concurrent import futures

import grpc
import math_pb2
import math_pb2_grpc


class Math(math_pb2_grpc.MathServicer):
    def get_sqrt(self, request, context):
        return math_pb2.SqrtResponse(sqrt=math.sqrt(request.number))

    def get_std(self, request_iterator, context):

        numbers = []

        for request in request_iterator:
            numbers.append(request.number)

        return math_pb2.StdResponse(std=statistics.stdev(numbers))

    def get_multipliers(self, request, context):
        multipliers = []
        n = request.number

        d = 2
        while d * d <= n:
            if n % d == 0:
                multipliers.append(d)
                n //= d
            else:
                d += 1

        if n > 1:
            multipliers.append(n)

        for multiplier in multipliers:
            yield math_pb2.MultipliersResponse(number=multiplier)

    def get_max(self, request_iterator, context):
        max_ = -math.inf

        for request in request_iterator:
            if request.number > max_:
                max_ = request.number

            yield math_pb2.MaxResponse(max=max_)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    math_pb2_grpc.add_MathServicer_to_server(Math(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
