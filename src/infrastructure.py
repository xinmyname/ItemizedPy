"""Holds all infrastructure related items"""

import models

class ItemFactory:
    """Creates items"""

    def make_item(self):
        """Creates items"""
        return models.Item()
