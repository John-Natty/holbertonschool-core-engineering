#!/usr/bin/env python3
"""Module that defines an islower function."""


def islower(c):
    """Return True if c is a lowercase letter, False otherwise."""
    return ord(c) >= 97 and ord(c) <= 122
