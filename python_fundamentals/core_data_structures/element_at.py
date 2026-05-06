#!/usr/bin/env python3
"""Safely access an element in a list."""


def element_at(my_list, idx):
    """Return an element from a list at a given index."""

    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
