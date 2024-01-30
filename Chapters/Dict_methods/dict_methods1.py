"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    dict1 = current_cart

    for item in items_to_add:
        dict1[item] = dict1.get(item, 0) + 1

    return dict1


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    dict1 = {}
    for item in notes:
        dict1[item] = dict1.get(item, 1)

    return dict1


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    dict1 = ideas
    dict1.update(recipe_updates)

    return dict1


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    dict1 = dict(sorted(cart.items()))

    return dict1


def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    list = []
    dict1 = {}
    for item in cart.keys():
        list.append([cart.get(item), isle_mapping.get(item)[0], isle_mapping.get(item)[1]])
    i = 0
    for item in cart.keys():
        dict1[item] = dict1.get(None, list[i])
        i += 1
    dict2 = dict(sorted(dict1.items(), reverse=True))

    return dict2


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    dict1 = fulfillment_cart
    dict2 = store_inventory
    # dict1 = dict(sorted(fulfillment_cart.items()))
    # dict2 = dict(sorted(store_inventory.items()))
    list_dict1 = []
    list_dict2 = []

    for key, value in dict1.items():
        list_dict1.append(value)

    for key, value in dict2.items():
        list_dict2.append(value)

    for item in dict1.keys():
        if dict2.get(item)[0] - dict1.get(item)[0] > 0:
            dict2[item] = [dict2.get(item)[0] - dict1.get(item)[0], dict2.get(item)[1], dict2.get(item)[2]]
        else:
            dict2[item] = ["Out of Stock", dict2.get(item)[1], dict2.get(item)[2]]

    return dict2
