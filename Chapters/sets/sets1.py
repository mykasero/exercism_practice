"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    tuple1 = (dish_name,set(dish_ingredients))

    return tuple1


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    drink = drink_name
    ingredients = set(drink_ingredients)
    has_alcohol = False

    for item in ALCOHOLS:
        if item in ingredients:
            has_alcohol = True
            break

    if has_alcohol:
        drink += " Cocktail"
    else:
        drink += " Mocktail"

    return drink

def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    name_and_type = dish_name
    ingredient_type = ""
    set_ingredients = set(dish_ingredients)
    if set_ingredients.issubset(VEGAN):
        ingredient_type = ": VEGAN"
    elif set_ingredients.issubset(VEGETARIAN):
        ingredient_type = ": VEGETARIAN"
    elif set_ingredients.issubset(PALEO):
        ingredient_type = ": PALEO"
    elif set_ingredients.issubset(KETO):
        ingredient_type = ": KETO"
    elif set_ingredients.issubset(OMNIVORE):
        ingredient_type = ": OMNIVORE"

    name_and_type += ingredient_type

    return name_and_type


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    ingredients = set(dish[1])
    special_ingredients = set(SPECIAL_INGREDIENTS)

    special = ingredients & special_ingredients

    name_and_special = (dish[0],special)

    return name_and_special


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """


    all_ingredients = set()

    for main_iter in range(0,len(dishes)):
        all_ingredients = all_ingredients.union(dishes[main_iter])



    return all_ingredients


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    set_main = set(dishes)
    set_sides = set(appetizers)
    set_final = set_main.difference(set_sides)


    return list(set_final)


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    singletons = set()
    for dish in dishes:
        dishes = dish-intersection
        singletons = singletons.union(dishes)
    return singletons
