#!/usr/bin/env python3
"""Module that defines a pow function."""


def pow(a, b):
    """Return a to the power of b."""
    result = 1
    for _ in range(b):
        result *= a
    return result
