from app.infrastructure.ItemFactory import *
from app.models.Inventory import *
from app.models.Slot import *

itemFactory = ItemFactory()
inventory = Inventory()

inventory.addItem(itemFactory.makeItem())
inventory.addItem(itemFactory.makeItem())
inventory.addItem(itemFactory.makeItem())

for slot in inventory.slots():
	print(slot)

