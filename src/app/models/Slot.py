"""Slot holds an item and a quantity"""

class Slot:
    """Slot holds an item and a quantity"""

    def __init__(self, item):

        self.quantity = 1
        self.item = item

    def __str__(self):

        if self.quantity == 1:
            text = "{0.item}".format(self)
        else:
            text = "{0.item}s".format(self)

        if self.quantity == 1:
            quantity_text = "An"
        elif self.quantity == 0:
            quantity_text = "No"
        elif self.quantity == 2:
            quantity_text = "Two"
        elif self.quantity == 3:
            quantity_text = "Three"
        elif self.quantity == 4:
            quantity_text = "Four"
        elif self.quantity == 5:
            quantity_text = "Five"
        elif self.quantity == 6:
            quantity_text = "Six"
        elif self.quantity == 7:
            quantity_text = "Seven"
        elif self.quantity == 8:
            quantity_text = "Eight"
        elif self.quantity == 9:
            quantity_text = "Nine"
        else:
            quantity_text = str(self.quantity)

        return "{} {}".format(quantity_text, text)
