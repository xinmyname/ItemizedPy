from .Item import *

class Slot:

	def __init__(self,item):

		self.quantity = 1
		self.item = item

	def __str__(self):

		if self.quantity == 1:
			text = "{0.item}".format(self)
		else:
			text = "{0.item}s".format(self)

		if self.quantity == 1:
			quantityText = "An"
		elif self.quantity == 0:
			quantityText = "No"
		elif self.quantity == 2:
			quantityText = "Two"
		elif self.quantity == 3:
			quantityText = "Three"
		elif self.quantity == 4:
			quantityText = "Four"
		elif self.quantity == 5:
			quantityText = "Five"
		elif self.quantity == 6:
			quantityText = "Six"
		elif self.quantity == 7:
			quantityText = "Seven"
		elif self.quantity == 8:
			quantityText = "Eight"
		elif self.quantity == 9:
			quantityText = "Nine"
		else:
			quantityText = str(self.quantity)

		return "{} {}".format(quantityText, text)


		