#!/usr/bin/env python3
"""Module to read a file"""


def read_file(filename: str) -> str:
    """Reads a file and returns its content as a string

    Args:
        filename (str): The name of the file to read

    Returns:
        str: The content of the file
    """
    with open(filename, 'r') as f:
        return f.read()
