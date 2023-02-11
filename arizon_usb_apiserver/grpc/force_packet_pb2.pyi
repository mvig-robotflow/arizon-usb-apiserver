from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor


class ForceGetFIFOStatusRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None: ...


class ForcePacketRequest(_message.Message):
    __slots__ = ["timestamp"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int

    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...


class ForcePacketResponse(_message.Message):
    __slots__ = ["addr", "f", "index", "sys_ts_ns", "valid"]
    ADDR_FIELD_NUMBER: _ClassVar[int]
    F_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SYS_TS_NS_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    addr: int
    f: float
    index: int
    sys_ts_ns: int
    valid: bool

    def __init__(self, addr: _Optional[int] = ..., f: _Optional[float] = ..., index: _Optional[int] = ..., sys_ts_ns: _Optional[int] = ..., valid: bool = ...) -> None: ...


class ForceResetCacheRequest(_message.Message):
    __slots__ = []

    def __init__(self) -> None: ...


class ForceSetFIFOStatusRequest(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool

    def __init__(self, status: bool = ...) -> None: ...


class ForceStatusResponse(_message.Message):
    __slots__ = ["err", "status"]
    ERR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    err: str
    status: bool

    def __init__(self, status: bool = ..., err: _Optional[str] = ...) -> None: ...
