#!/usr/bin/env python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file.

    Return the number of characters added.
    """
    # Open the file in append mode.
    # Mode "a" creates the file if needed and writes at the end.
    with open(filename, "a", encoding="utf-8") as file:
        # write() appends the text and returns the number of characters written
        return file.write(text)
