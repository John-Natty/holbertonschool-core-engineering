#!/usr/bin/env python3
"""Replace an element in a list at a specific position."""


def replace_in_list(my_list, idx, element):
    """Replace an element at a given index in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
