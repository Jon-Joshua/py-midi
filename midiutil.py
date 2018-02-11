import struct

# Read byte and return as byte
def _read_byteb(byte_s):
    return byte_s.read(1)


# Read single byte and return as integer
def _read_byte_i(byte_s):
    return int.from_bytes(byte_s.read(1), byteorder='big')


# Return bytes in list of integers
def _read_bytes_l(byte_s, length):
    byte_list = []
    for x in range(length):
        byte_list.append(_read_byte_i(byte_s))
    return byte_list


# Read bytes and return as python string
def _read_bytes_s(byte_s, length):
    string = b''
    for x in range(length):
        string += _read_byteb(byte_s)
    return string.decode('ISO 8859-1')


# Read bytes and return as byte string
def _read_bytes(byte_s, length):
    string = b''
    for x in range(length):
        string += _read_byteb(byte_s)
    return string


def _get_chunkb(byte_s):
    header = _read_bytes(byte_s, 8)
    return struct.unpack('>4sI', header)


""" Decode variable length value
    If byte is more than 0x80 continue getting bytes and adding to value.
"""
def _read_vlenb(byte_s):
    value = 0x00
    while True:
        byte = _read_byte_i(byte_s)
        value += byte

        if byte <= 0x80:
            break
    return value
