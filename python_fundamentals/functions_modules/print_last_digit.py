#!/usr/bin/env python3
"""Module that defines a print_last_digit function."""


def print_last_digit(number):
    """Print and return the last digit of a number."""
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
