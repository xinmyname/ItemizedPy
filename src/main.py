from optparse import OptionParser
from app.infrastructure.ItemFactory import *
from app.models.Inventory import *
from app.models.Slot import *

numItems = 1

parser = OptionParser("Usage: %prog [count]")

(options,args) = parser.parse_args()

if len(args) > 0:
	numItems = int(args[0])

itemFactory = ItemFactory()
inventory = Inventory()

while numItems > 0:
	inventory.addItem(itemFactory.makeItem())
	numItems -= 1

for slot in inventory.slots():
	print(slot)
