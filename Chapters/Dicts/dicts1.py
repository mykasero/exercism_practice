"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    dict1 = {}

    for item in items:
        dict1[item] = items.count(item)

    return dict1


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    dict1 = {}
    dict2 = inventory

    for item in items:
        dict2[item] = dict2.get(item, 0)+1

    return dict2


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    dict1 = inventory
    for item in items:
        if dict1[item] > 0:
            dict1[item] = dict1.get(item,0) - 1

    return dict1

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    dict1 = inventory
    if dict1.get(item,0) != 0:
        dict1.pop(item)
    else:
        pass

    return dict1

def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    items = []

    for key in inventory.keys():
        if inventory.get(key,0) !=0:
            items.append((key,inventory.get(key)))

    return items

