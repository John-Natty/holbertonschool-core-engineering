#!/usr/bin/env python3
"""Print all integers of a list."""


def print_list_integer(my_list=[]):
    """Print each integer of a list, one per line."""
    for integer in my_list:
        print("{:d}".format(integer))
