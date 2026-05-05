#!/usr/bin/env python3
"""Program that imports add and prints the result of 1 + 2."""

from add_0 import add


if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)

    print("{} + {} = {}".format(a, b, result))
