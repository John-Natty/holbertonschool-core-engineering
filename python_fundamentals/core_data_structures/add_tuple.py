#!/usr/bin/env python3
"""Add two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Add the first two values of two tuples."""
    valeur_a_0 = 0
    valeur_a_1 = 0
    valeur_b_0 = 0
    valeur_b_1 = 0

    if len(tuple_a) > 0:
        valeur_a_0 = tuple_a[0]
    if len(tuple_a) > 1:
        valeur_a_1 = tuple_a[1]
    if len(tuple_b) > 0:
        valeur_b_0 = tuple_b[0]
    if len(tuple_b) > 1:
        valeur_b_1 = tuple_b[1]
    return (valeur_a_0 + valeur_b_0, valeur_a_1 + valeur_b_1)
