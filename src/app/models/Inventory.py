"""Holds inventory"""
from .Slot import Slot

class Inventory:
    """Holds inventory"""

    def __init__(self):
        self.__slots = {}

    def add_item(self, item):
        """Adds an item to the inventory"""

        if item.descriptor in self.__slots:
            slot = self.__slots[item.descriptor]
            slot.quantity += 1
        else:
            self.__slots[item.descriptor] = Slot(item)

    def slots(self):
        """Returns a list of slots"""
        return self.__slots.values()
