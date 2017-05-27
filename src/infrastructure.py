"""Holds all infrastructure related items"""

from models import Item

class ItemFactory:
    """Creates items"""

    def make_item(self):
        """Creates items"""
        return Item()
