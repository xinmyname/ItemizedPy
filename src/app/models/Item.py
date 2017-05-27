"""An item"""
from .Descriptor import Descriptor

class Item:
    """An item"""

    def __init__(self):
        self.descriptor = Descriptor()

    def __str__(self):
        return "item"
