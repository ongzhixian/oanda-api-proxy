
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
from protos.helloworld_pb2 import HelloReply
from protos.helloworld_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server

from protos.basic_example_pb2 import BasicExampleResponse
from protos.basic_example_pb2_grpc import BasicExampleServicer, add_BasicExampleServicer_to_server

from logger import Logger

log = Logger()


class Greeter(GreeterServicer):
    def SayHello(self, request, context):
        return HelloReply(message='Hello, %s!' % request.name)


class Four_Modes(BasicExampleServicer):
    def UnaryApi(self, request, context):
        log.info("Unary API")
        log.info(f"Requests - {request}")
        # print(dir(request))
        # ['ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DESCRIPTOR', 'DiscardUnknownFields', 'Extensions', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', '_SetListener', '__class__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__unicode__', '_extensions_by_name', '_extensions_by_number', 'request_purpose']
        res = BasicExampleResponse(message="Unary Response is here!")
        log.info(f"Response - {res}")
        return res

    def ServerStreamingApi(self, request, context):
        log.info("ServerStreaming API")
        log.info(f"Request - {request}")
        for i in range(10):
            res = BasicExampleResponse(message=f"Stream Response : {i + 1}")
            log.info(f"Response - {res}")
            yield res

    def ClientStreamingApi(self, request_iterator, context):
        log.info("Client Streaming API")
        for r in request_iterator:
            log.info(f"Request - {r}")

        res = BasicExampleResponse(message="Response for your stream requests")
        log.info(f"Response - {res}")
        return res

    def BiDirectionalStreamingApi(self, request_iterator, context):
        log.info("Bi-Directional Streaming API")
        for r in request_iterator:
            log.info(f"Request - {r}")
            res = BasicExampleResponse(message=f"Response for your stream requests : {r.request_purpose}")
            log.info(f"Response - {res}")
            yield res



def serve_grpc():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Greeter(), server)
    add_BasicExampleServicer_to_server(Four_Modes(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    log.info("Grpc server started", port=port)
    server.wait_for_termination()
