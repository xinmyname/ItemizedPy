"""Creates items and adds them an inventory."""
import argparse
from infrastructure import ItemFactory
from infrastructure import plural_of
from models import Inventory

def main(args):
    """Run the program"""

    #print(plural_of("word"))
    #exit()

    num_items = args.count

    item_factory = ItemFactory()
    inventory = Inventory()

    while num_items > 0:
        inventory.add_item(item_factory.make_item())
        num_items -= 1

    print("You have:")
    print("")

    for slot in inventory.slots():
        print("  {}".format(slot))

PARSER = argparse.ArgumentParser(description="Creates items and adds them an inventory.")

PARSER.add_argument('count', metavar='count', type=int, nargs='?',
                    default=1, help='Number of items')

main(PARSER.parse_args())
