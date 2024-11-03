#!/usr/bin/python3
"""This module contains a function that determines if a given data set
represents a valid UTF-8 encoding.
"""


def byte_length(byte):
    """Determines the number of bytes in a UTF-8 character based
    on the first byte.
    """
    if byte & 0b10000000 == 0b00000000:
        return 1  # 1-byte character
    elif byte & 0b11100000 == 0b11000000:
        return 2  # 2-byte character
    elif byte & 0b11110000 == 0b11100000:
        return 3  # 3-byte character
    elif byte & 0b11111000 == 0b11110000:
        return 4  # 4-byte character
    else:
        return -1


def validUTF8(data):
    """This function determines if data set is
        a valid UTF-8 encoding.
    """
    i = 0
    while i < len(data):
        # get the number of UTF-8 character bytes by bit masking
        number_of_bytes = byte_length(data[i])
        # invalid byte
        if number_of_bytes == -1:
            return False

        for j in range(1, number_of_bytes):
            if ((i + j >= len(data)) or
                    (data[i + j] & 0b11000000) != 0b10000000):
                return False
        i += number_of_bytes
    return True
