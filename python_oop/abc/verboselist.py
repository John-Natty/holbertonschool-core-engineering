#!/usr/bin/env python3
"""Module for a verbose list class."""


class VerboseList(list):
    """List subclass that prints messages when modified."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print(f"Appended {item} to the list.")

    def extend(self, items):
        """Extend the list and print a notification."""
        super().extend(items)
        print(f"Extended the list with {items}.")

    def remove(self, item):
        """Remove an item and print a notification."""
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """Pop an item and print a notification."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
