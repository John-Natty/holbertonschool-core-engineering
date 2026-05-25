#!/usr/bin/env python3


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file"""
    # Open the file in append mode with UTF-8 encoding
    with open(filename, "a", encoding="utf-8") as file:
        """returns the number of characters added to the file"""
        # Write the text to the file and get the number of characters written
        return file.write(text)
