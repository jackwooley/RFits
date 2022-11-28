import random
import pandas as pd
import re


def category_keys():
    """Create a dictionary with keys and no values. Keys correspond to
     different clothing categories.
    """

    # type_list = list(str(input("""Enter a comma-separated list of the different clothing categories you'd like to include.""")).split(', '))

    clothing_type_inputs = str(input("""Enter a comma-separated list of the different clothing categories you'd like to include."""))
    type_list = re.split(",\s*", clothing_type_inputs)

    clothes_dict = {}
    for i in range(0, len(type_list)):
        clothes_dict[type_list[i]] = ''
    return clothes_dict


test_dict = category_keys()


def in_my_closet(which_dict: dict):

    # todo: add a

    """Add the clothes values into the previously created dictionary.

    Keyword arguments:
    which_dict -- what dictionary the function should modify
    # clothes_types -- a list of all the clothing types you want to modify
    # all_the_clothes -- a list of all the clothing types (the values in the
    # key-value pair of {'clothes category': ['clothing item 1']})
    """

    # for i in clothes_types:
    #     list1 = list(str(input(f"Enter a comma-separated list of clothing items in the {i} category.")).split(", "))

    for j in which_dict.keys():
        input_for_choosing = str(input(f"Enter a comma-separated list of clothing items in the {j} category."))
        which_dict[j] = re.split(",\s*", input_for_choosing)

        # which_dict[j] = list(str(input(f"Enter a comma-separated list of clothing items in the {j} category.")).split(", "))

    return which_dict


in_my_closet(test_dict)


def outfit_selector_function(closet: dict):

    input_for_choosing = str(input("""Enter a comma-separated list of categories you want to choose from."""))
    choose_from = re.split(",\s*", input_for_choosing)

    new_fit = {}

    for i in choose_from:
        new_fit[i] = random.choice(closet[i])

    return new_fit


blind = outfit_selector_function(test_dict)

print('for debugging')
