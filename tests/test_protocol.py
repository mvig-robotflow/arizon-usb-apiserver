import serial
import numpy as np
import struct
import logging
from typing import List, Dict, Tuple, AnyStr, BinaryIO, Union
from io import BytesIO
from arizon_usb_driver import Parser

if __name__ == '__main__':
    pass
    p = Parser()
    res = p.submit_buffer(bytearray([0xfe, 0x11, 0x00, 0x01, 0xa8, 0x46]))
    print(res)
