from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BasicExampleRequest(_message.Message):
    __slots__ = ["action_name"]
    ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    action_name: str
    def __init__(self, action_name: _Optional[str] = ...) -> None: ...

class BasicExampleResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
