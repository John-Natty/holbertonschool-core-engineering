#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square."""
    def __init__(self, size=0):
        """Initialize Square with size validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
