#!/usr/bin/env python3

def safe_print_division(a, b):
    """Perform safe division of two numbers.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        float: The result of the division,
        or None if division cannot be performed.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
