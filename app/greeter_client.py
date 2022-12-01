
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
from protos import helloworld_pb2
from protos import helloworld_pb2_grpc

import protos.basic_example_pb2_grpc as my_grpc
import protos.basic_example_pb2 as my_pb

log = logging.getLogger(__name__)


# socket = 'localhost:50051'
# channel = grpc.insecure_channel(socket)
# client = my_grpc.BasicExampleStub(channel)


# def make_unary_request(request_string: str):
#     log.info("Making Unary Request")
#     pb_req = my_pb.BasicExampleRequest(action_name=request_string)
#     log.info(f"Request - {pb_req}")
#     u_res = client.UnaryApi(pb_req)
#     log.info(f"Response - {u_res}")


# def make_server_streaming_request(request_string: str):
#     log.info("making Server Streaming Request")
#     pb_req = my_pb.BasicExampleRequest(action_name=request_string)
#     log.info(f"Request - {pb_req}")
#     # for response in client.ServerStreamingAPI(pb_req):
#     #     log.info(f"Response - {response}")
#     ### Both works
#     res = client.ServerStreamingApi(pb_req)
#     for r in res:
#         log.info(f"Response - {r}")


# def make_client_streaming_request(request_string_list: list):
#     log.info("Making Client Streaming request")
#     pb_req_list = []
#     for req_str in request_string_list:
#         pb_req_list.append(my_pb.BasicExampleRequest(action_name=req_str))
#     log.info(f"Request - {pb_req_list}")
#     cs_res = client.ClientStreamingApi(pb_req_list.__iter__())
#     log.info(f"Response - {cs_res}")


# def make_bidirectional_stream_request(request_string_list: list):
#     log.info("Making Bi-Directional Streaming request")
#     pb_req_list = []
#     for req_str in request_string_list:
#         pb_req_list.append(my_pb.BasicExampleRequest(action_name=req_str))
#     log.info(f"Request - {pb_req_list}")
#     for bi_res in client.DuplexStreamingApi(pb_req_list.__iter__()):
#         log.info(f"Response - {bi_res}")


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # print("Will try to greet world ...")
    # with grpc.insecure_channel('127.0.0.1:50051') as channel:
    #     stub = helloworld_pb2_grpc.GreeterStub(channel)
    #     response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    # print("Greeter client received: " + response.message)

    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        client = my_grpc.BasicExampleStub(channel)
        # response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Making Unary Request")
        pb_req = my_pb.BasicExampleRequest(action_name='some request string')
        print(f"Request - {pb_req}")
        u_res = client.UnaryApi(pb_req)
        print(f"Response - {u_res}")


    # make_server_streaming_request("Need stream response")

    # make_client_streaming_request(["Client stream 1", "client stream 2", "Client Stream 3"])

    # make_bidirectional_stream_request(["Bi-Directional req stream 1", "Bi-Directional req  stream 2"])

if __name__ == '__main__':
    logging.basicConfig()
    run()


# https://betterprogramming.pub/grpc-file-upload-and-download-in-python-910cc645bcf0
# https://github.com/techunits?tab=repositories&q=grpc&type=&language=&sort=
