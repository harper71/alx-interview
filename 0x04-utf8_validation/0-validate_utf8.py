#!/usr/bin/python3
"""utf-8 validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determines if a list of integers represents a valid UTF-8 encoding.

    UTF-8 encoding can be 1 to 4 bytes long:
      - 1-byte: starts with 0xxxxxxx
      - 2-byte: starts with 110xxxxx 10xxxxxx
      - 3-byte: starts with 1110xxxx 10xxxxxx 10xxxxxx
      - 4-byte: starts with 11110xxx 10xxxxxx
      10xxxxxx 10xxxxxx

    Parameters:
    - data (List[int]): A list of integers, where each integer represents
      a byte (8 bits) in the range 0 to 255.

    Returns:
    - bool: True if `data` represents a valid UTF-8 encoding, False otherwise.

    Internal Functions:
    - Check(num: int) -> int:
        Checks how many leading 1s are present in the byte,
        `num`.
        This is used to determine the expected
        number of bytes in a UTF-8 character.

    Logic:
    - The function iterates over each byte in `data`.
    - It uses the Check function to determine the
    expected byte count for the UTF-8 character starting at each index.
    - It then verifies if the subsequent bytes follow
    the expected UTF-8 continuation pattern.
    - If any invalid UTF-8 encoding is found,
    the function returns False.

    Example:
    >>> validUTF8([197, 130, 1])
    True
    >>> validUTF8([235, 140, 4])
    False
    """

    def Check(num):
        """
        Determines the number of leading 1s in the byte `num`.

        Parameters:
        - num (int): The byte to be checked.

        Returns:
        - int: Number of leading 1 bits in `num`.
          - If 0, this byte represents an ASCII character.
          - If 1-4, this byte indicates the start of a UTF-8 character
            of the corresponding length.
        """

        mask = 1 << (8-1)
        i = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i
    i = 0

    while i < len(data):
        j = Check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            current = Check(data[i])
            if current != 1:
                return False
            i += 1

    return True
