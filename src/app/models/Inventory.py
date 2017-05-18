from .Slot import *

class Inventory:

	def __init__(self):
		self.__slots = {}
	
	def addItem(self, item):

		if item.descriptor in self.__slots:
			slot = self.__slots[item.descriptor]
			slot.quantity += 1
		else:
			self.__slots[item.descriptor] = Slot(item)

	def slots(self):
		return self.__slots.values()