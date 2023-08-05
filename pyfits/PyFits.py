import random
# import pandas as pd
import re
import json


def main():
    
    # check if closet.json exists or not
    # if it doesn't, input the new closet
    # if it does, ask if you want to modify it
    
    # if does_json_exist():
    
    MODIFY_WRITE_OR_IGNORE_PARAMETER = str(input("""Enter the letter w to create or completely overwrite your current closet, a to append new values, d to delete values, \nor any other letter to skip this step if you are happy with what is currently in it."""))
    
    # fill up the closet with clothing items (values)
    # full_closet = fill_my_closet(closet_keys, MODIFY_WRITE_OR_IGNORE_PARAMETER)
    full_closet = {}

    # change the mode string to lower and make sure it's an accepted input
    which_mode_lower = MODIFY_WRITE_OR_IGNORE_PARAMETER.lower()
    if which_mode_lower == 'w':
        CLOTHING_TYPES = str(input("""Enter a comma-separated list of the different clothing categories you'd like to include."""))
        # fill up the closet with clothing types (keys)
        closet_keys = category_keys(CLOTHING_TYPES)
        fill_my_closet(closet_keys, full_closet, which_mode_lower)
        write_closet_to_json(full_closet, which_mode_lower)
        with open('closet.json') as json_file:
            closet = json.load(json_file)
    elif which_mode_lower == 'a':
        with open('closet.json') as json_file:
            closet = json.load(json_file)
        keys_to_modify = str(input(
            f"""Which clothing categories would you like to add new items to? Your options are: {re.sub("'", '', str(closet.keys())[11:-2])}. Enter a comma-separated list: """))
        list_of_keys_to_modify = re.split("\s*,\s*", keys_to_modify)
        # modify_closet_json(list_of_keys_to_modify)
        update_closet(list_of_keys_to_modify)
        print('sdfa')
        with open('closet.json') as json_file:
            closet = json.load(json_file)
    elif which_mode_lower == 'd':
        with open('closet.json') as json_file:
            closet = json.load(json_file)
        deleter()
        with open('closet.json') as json_file:
            closet = json.load(json_file)
    else:
        with open('closet.json') as json_file:
            closet = json.load(json_file)

    # pick a fit 😎
    random_fit = outfit_selector_function(closet=closet)
    print(random_fit)

    #TODO -- set up a laundry bin
    
        



def category_keys(clothing_type_inputs: str):
    """Create a dictionary with keys and no values. Keys correspond to 
    different clothing categories.
    """

    type_list = re.split("\s*,\s*", clothing_type_inputs)

    clothes_dict = {}
    for i in range(0, len(type_list)):
        clothes_dict[type_list[i]] = ''
    return clothes_dict


# test_dict = category_keys()


def fill_my_closet(dict_with_info: dict, dict_to_modify: dict, mode: str):
    """Add the clothes values into the previously created dictionary.

    Keyword arguments:
    dict_with_info -- a dictionary with the keys whose values you are trying to modify
    dict_to_modify -- what dictionary the function should modify
    clothes_types -- a list of all the clothing types you want to modify
    all_the_clothes -- a list of all the clothing types (the values in the
    key-value pair of {'clothes category': ['clothing item 1']})
    """

    for j in dict_with_info.keys():
        input_for_choosing = str(input(f"Enter a comma-separated list of clothing items in the {j} category."))
        dict_to_modify[j] = re.split("\s*,\s*", input_for_choosing)

    write_closet_to_json(dict_to_modify, mode)

    return dict_to_modify


def does_json_exist():
    """Check if closet.json exists.
    """
    try:
        with open('closet.json') as outfile:
            closet = json.load(outfile)
            return True
    except BaseException as be:  # change this error type to be more specific
        print('Does closet.json exist?')
        return False


def write_closet_to_json(closet_dict: dict, which_mode: str):
    # write the dict to a json so that you can save it and edit it later
    with open('closet.json', which_mode) as outfile:
        json.dump(closet_dict, outfile)
#
#
# def modify_closet_json(closet_dict: dict, *args):
#     # todo: add a section to open the json as a dictionary
#     with open('closet.json') as json_file:
#         closet = json.load(json_file)
#
#     # append the input to each category
#     for i in args:
#         closet_dict[i].append(re.split(",\s*", input(f"""What do you want to add to the {i} category? Enter a comma-separated list.""")))

def update_closet(clothing_types_to_update: list):
    try:
        with open('closet.json') as json_file:
            closet_to_modify = json.load(json_file)
        for type_ in clothing_types_to_update:
            values_to_modify = str(input(
                f"""What would you like to add to the {type_} clothing field? Enter a comma-separated list."""))
            list_to_append = re.sub('\s*,\s*', ',', values_to_modify).split(',')
            closet_to_modify[type_] = [*closet_to_modify[type_], *list_to_append]
    except AttributeError or FileNotFoundError as af:
        print('bro the file doesn\'t seem to exist lol')
        raise af
    
    write_closet_to_json(closet_to_modify, 'w')

    print('Updated closet.json')


def delete_keys(key_to_delete: str, closet_dict: dict):
    if key_to_delete in closet_dict.keys():
        del(closet_dict[key_to_delete])
        print(f'Key {key_to_delete} deleted successfully.')
    return closet_dict


def delete_values(value_to_delete: str, key_to_delete_from: str, closet_dict: dict):
    if value_to_delete in closet_dict[key_to_delete_from]:
        del(closet_dict[key_to_delete_from][closet_dict[key_to_delete_from] == value_to_delete])
        print(f'Value {value_to_delete} deleted successfully.')
    return closet_dict


def deleter():
    with open('closet.json') as json_file:
            closet_to_modify = json.load(json_file)

    k_to_delete = str(input(
        f"""Which keys would you like to delete? Your options are: {re.sub("'", '', str(closet_to_modify.keys())[11:-2])}. Enter comma-separated values. """))
    k_to_delete = re.sub('\s*,\s*', ',', k_to_delete).split(',')
    for deleted in k_to_delete:
        closet_to_modify = delete_keys(deleted, closet_to_modify)

    kv_to_delete = re.sub('\s*,\s*', ',', str(input(  # TODO -- standardize how these string things are set up and split into lists
        f"""Which keys would you like to delete values from? Your options are: {re.sub("'", '', str(closet_to_modify.keys())[11:-2])}. Enter comma-separated values: """))).split(',')

    for kv in kv_to_delete:
        v_to_delete = str(input(
            f"""Which values would you like to delete from {str(kv)}? Your options are: {re.sub("'", '', str(closet_to_modify[kv])[2:-2])}. Enter comma-separated values: """))
        v_to_delete = re.sub('\s*,\s*', ',', v_to_delete).split(',')
        for deleted_ in v_to_delete:
            closet_to_modify = delete_values(deleted_, kv, closet_to_modify)

    write_closet_to_json(closet_to_modify, 'w')


def outfit_selector_function(closet: dict):

    input_for_choosing = str(input("""Enter a comma-separated list of categories you want to choose from."""))
    choose_from = re.split("\s*,\s*", input_for_choosing)

    new_fit = {}

    for i in choose_from:
        new_fit[i] = random.choice(closet[i])

    # if new_fit[item] in dirty_laundry:
    #   resample

    return new_fit


# blind = outfit_selector_function(test_dict)

print('for debugging')


if __name__ == "__main__":
    main()
