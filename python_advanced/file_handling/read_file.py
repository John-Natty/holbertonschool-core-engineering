#!/usr/bin/env python3
"""Module for reading a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    # Open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        # Read the whole content of the file
        content = file.read()

        # Print the content without adding an extra newline
        print(content, end="")
