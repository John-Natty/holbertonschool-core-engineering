#!/usr/bin/env python3
"""Square class"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """__init__ method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """__str__ method"""
        return f"[Square] {self.__size}/{self.__size}"
