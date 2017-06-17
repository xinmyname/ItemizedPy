"""Creates items and adds them an inventory."""
import argparse
import infrastructure
import models

def main(args):
    """Run the program"""

    num_items = args.count

    item_factory = infrastructure.ItemFactory()
    inventory = models.Inventory()

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
