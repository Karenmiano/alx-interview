#!/usr/bin/python3
"""
Defines the function validUTF8
"""


def validUTF8(data):
    """
    Checks if an array of integers represents a valid utf-8 encoding.
    """
    continuation_bytes = 0

    for value in data:
        if continuation_bytes > 0:
            if value >> 6 != 0b10:
                return False
            continuation_bytes -= 1
        else:
            if value >> 7 == 0:
                continue
            elif value >> 5 == 0b110:
                continuation_bytes = 1
            elif value >> 4 == 0b1110:
                continuation_bytes = 2
            elif value >> 3 == 0b11110:
                continuation_bytes = 3
            else:
                return False

    return continuation_bytes == 0
