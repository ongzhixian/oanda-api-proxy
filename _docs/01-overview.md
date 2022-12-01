# Overview

Oanda API proxy

## Setup

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip


python -m grpc_tools.protoc -I./protos --python_out=./protos --pyi_out=./protos --grpc_python_out=./protos helloworld.proto


