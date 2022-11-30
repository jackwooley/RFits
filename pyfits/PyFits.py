import random
# import pandas as pd
from re import split
import json

CLOTHING_TYPES = str(
    input("""Enter a comma-separated list of the different clothing categories you'd like to include."""))
MODIFY_WRITE_OR_IGNORE_PARAMETER = str(input("""Enter the letter w to create or overwrite your current closet, a to modify, \nor any other letter to skip this step if you are happy with what is currently in it."""))


def main():
    # fill up the closet with clothing types (keys)
    closet_keys = category_keys(CLOTHING_TYPES)

    # fill up the closet with clothing items (values)
    full_closet = fill_my_closet(closet_keys, MODIFY_WRITE_OR_IGNORE_PARAMETER)

    # change the mode string to lower and make sure it's an accepted input
    which_mode_lower = MODIFY_WRITE_OR_IGNORE_PARAMETER.lower()
    if ord(which_mode_lower) == 119:
        write_closet_to_json(full_closet, which_mode_lower)
    elif ord(which_mode_lower) == 97:
        keys_to_modify = str(
        input("""Which clothing categories would you like to update? Enter a comma-separated list."""))
        list_of_keys_to_modify = split(",\s*", keys_to_modify)
        modify_closet_json(list_of_keys_to_modify)


def category_keys(clothing_type_inputs: str):
    """Create a dictionary with keys and no values. Keys correspond to
     different clothing categories.
    """

    type_list = split(",\s*", clothing_type_inputs)

    clothes_dict = {}
    for i in range(0, len(type_list)):
        clothes_dict[type_list[i]] = ''
    return clothes_dict


# test_dict = category_keys()


def fill_my_closet(which_dict: dict, mode: str):
    """Add the clothes values into the previously created dictionary.

    Keyword arguments:
    which_dict -- what dictionary the function should modify
    # clothes_types -- a list of all the clothing types you want to modify
    # all_the_clothes -- a list of all the clothing types (the values in the
    # key-value pair of {'clothes category': ['clothing item 1']})
    """

    for j in which_dict.keys():
        input_for_choosing = str(input(f"Enter a comma-separated list of clothing items in the {j} category."))
        which_dict[j] = split(",\s*", input_for_choosing)

    write_closet_to_json(which_dict, mode)

    return which_dict


def write_closet_to_json(closet_dict: dict, which_mode: str):
    # write the dict to a json so that you can save it and edit it later
    with open('closet.json', which_mode) as outfile:
        json.dump(closet_dict, outfile)


def modify_closet_json(closet_dict: dict, *args):
    # todo: add a section to open the json as a dictionary

    # append the input to each category
    for i in args:
        closet_dict[i].append(split(",\s*", input(f"""What do you want to add to the {i} category? Enter a comma-separated list.""")))


def outfit_selector_function(closet: dict):

    input_for_choosing = str(input("""Enter a comma-separated list of categories you want to choose from."""))
    choose_from = split(",\s*", input_for_choosing)

    new_fit = {}

    for i in choose_from:
        new_fit[i] = random.choice(closet[i])

    return new_fit


# blind = outfit_selector_function(test_dict)
#
# print('for debugging')
