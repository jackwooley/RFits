import random
# import pandas as pd
from re import split
import json

# CLOTHING_TYPES = str(
#     input("""Enter a comma-separated list of the different clothing categories you'd like to include."""))
CLOTHING_TYPES = 'c1, c2, c3'

def main():
    # fill up the closet with clothing types (keys)
    closet_keys = category_keys(CLOTHING_TYPES)


    # fill up the closet with clothing items (values)
    # full_closet = fill_my_closet(closet_keys)
    full_closet = {}

    print('sdfa')


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

#
# def fill_my_closet(which_dict: dict):
#     """Add the clothes values into the previously created dictionary.
#
#     Keyword arguments:
#     which_dict -- what dictionary the function should modify
#     """
#
#     for j in which_dict.keys():
#         input_for_choosing = str(input(f"Enter a comma-separated list of clothing items in the {j} category."))
#         which_dict[j] = split(",\s*", input_for_choosing)
#
#     write_closet_to_json(which_dict)
#
#     return which_dict
#
#
# def write_closet_to_json(closet_dict: dict):
#     # write the dict to a json so that you can save it and edit it later
#     with open('closet.json') as outfile:
#         json.dump(closet_dict, outfile)
# #
# #
# # def modify_closet_json(closet_dict: dict, *args):
# #     # todo: add a section to open the json as a dictionary
# #     with open('closet.json') as json_file:
# #         closet = json.load(json_file)
# #
# #     # append the input to each category
# #     for i in args:
# #         closet_dict[i].append(split(",\s*", input(f"""What do you want to add to the {i} category? Enter a comma-separated list.""")))
#
#
# def outfit_selector_function(closet: dict):
#
#     input_for_choosing = str(input("""Enter a comma-separated list of categories you want to choose from."""))
#     choose_from = split(",\s*", input_for_choosing)
#
#     new_fit = {}
#
#     for i in choose_from:
#         new_fit[i] = random.choice(closet[i])
#
#     # if new_fit[item] in dirty_laundry:
#     #   resample
#
#     return new_fit
#
#
# # blind = outfit_selector_function(test_dict)
#
# print('for debugging')

if __name__ == "__main__":
    main()
