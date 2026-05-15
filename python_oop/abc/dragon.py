#!/usr/bin/env python3
"""Module for mixins with Dragon class."""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon with swimming and flying abilities."""

    def roar(self):
        """Print dragon roaring behavior."""
        print("The dragon roars!")
