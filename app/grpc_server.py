
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
from protos.helloworld_pb2 import HelloReply
from protos.helloworld_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server

from logger import Logger

log = Logger()


class Greeter(GreeterServicer):

    def SayHello(self, request, context):
        return HelloReply(message='Hello, %s!' % request.name)


def serve_grpc():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    log.info("Grpc server started", port=port)
    server.wait_for_termination()
