import numpy as np
import struct
from typing import List, Tuple, BinaryIO, Union
from io import BytesIO

class Parser:
    ADDR = 0xfe
    BLOCK_SZ: int = 0x1000
    PACKET_FMT = "1c1B3s1c"
    PACKET_LENGTH: int = struct.calcsize(PACKET_FMT)

    buffer: BinaryIO = BytesIO()

    def __init__(self) -> None:
        self.buf: np.ndarray = np.zeros(shape=(self.BLOCK_SZ), dtype=np.uint8)
        self.cursor: int = 0
        self.start_reg: int = 0
        self.length: int = 0
        self.data_valid: bool = False

    @staticmethod
    def sext24(d: bytes):
        """Convert 24-bit signed integer to 32-bit signed integer.

        Args:
            d (bytearray): bytes

        Returns:
            int: integer
        """
        if d[0] & 0x80:
            d = bytearray([0xff]) + d
        else:
            d = bytearray([0x00]) + d
        return struct.unpack('>i', d)[0]

    @classmethod
    def verify_packet(cls, data: bytes):
        return np.bitwise_xor.reduce(np.frombuffer(data[:-1], dtype=np.uint8)) == data[-1]

    @classmethod
    def parse_packet(cls, data: bytes) -> Union[None, np.uint16]:
        st = struct.unpack(cls.PACKET_FMT, data)
        n_digit = st[1] % 0x10
        value = cls.sext24(st[2])
        return value * 10 ** -n_digit

    def sync(self, buffer: bytes) -> Tuple[bool, List[Union[None, np.ndarray]]]:
        self.buffer.write(buffer)
        self.buffer.seek(0)

        while True:
            flag = self.buffer.read(1)
            if len(flag) != 1:
                return False, []
            if flag[0] == self.ADDR:
                self.buffer.seek(self.buffer.tell() - 1)
                break

        pkt = self.buffer.read(self.PACKET_LENGTH)
        if len(pkt) != self.PACKET_LENGTH:
            return False, []

        data_valid = self.verify_packet(pkt)
        if data_valid:
            res = [self.parse_packet(pkt)]
            while True:
                pkt = self.buffer.read(self.PACKET_LENGTH)
                if len(pkt) < self.PACKET_LENGTH:
                    self.buffer = BytesIO(pkt)
                    self.buffer.read()  # move pointer to end
                    break
                res.append(self.parse_packet(pkt))
            return True, res
        else:
            return False, []

    def submit_buffer(self, buffer: bytes) -> List[Union[None, np.ndarray]]:
        success, res = self.sync(buffer)
        self.state = "synced" if success else "unsynced"
        return res

