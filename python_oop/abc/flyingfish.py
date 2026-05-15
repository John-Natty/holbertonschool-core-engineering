#!/usr/bin/env python3
"""Module for multiple inheritance with Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represent a fish."""

    def swin(self):
        """Print how the fish swins."""
        print("The fish is swimming")

    def habitat(self):
        """Print where the fish lives."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print how the bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Print where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish."""

    def swim(self):
        """Print how the flying fish swims."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print how the flying fish flies."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print where the flying fish lives."""
        print("The flying fish lives both in water and the sky!")
