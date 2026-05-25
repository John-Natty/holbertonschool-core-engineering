#!/usr/bin/env python3
"""Module for writing to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file """
    # Open the file in write mode with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as file:
        """returns the number of characters written to the file"""
        # Write the text to the file and get the number of characters written
        return file.write(text)
