"""Creates items and adds them an inventory."""
import argparse
from app.infrastructure.ItemFactory import ItemFactory
from app.models.Inventory import Inventory

def run(args):
    """Run the program"""

    num_items = args.count

    item_factory = ItemFactory()
    inventory = Inventory()

    while num_items > 0:
        inventory.addItem(item_factory.makeItem())
        num_items -= 1

    print("You have:")
    print("")

    for slot in inventory.slots():
        print("  {}".format(slot))

PARSER = argparse.ArgumentParser(description="Creates items and adds them an inventory.")

PARSER.add_argument('count', metavar='count', type=int, nargs='?',
                    default=1, help='Number of items')

run(PARSER.parse_args())
