"""Holds all infrastructure related items"""

from models import Item

class ItemFactory:
    """Creates items"""

    def make_item(self):
        """Creates items"""
        return Item()

def plural_of(word):
    """Makes a singular word plurals"""
    return word

