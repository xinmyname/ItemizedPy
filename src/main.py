from app.infrastructure.ItemFactory import ItemFactory
from app.models.Inventory import Inventory
from app.models.Slot import Slot

itemFactory = ItemFactory()
item = itemFactory.makeItem()

print(item.toString())