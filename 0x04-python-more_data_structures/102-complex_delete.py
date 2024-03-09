#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for dict_value in list_keys:
        if a_dictionary[dict_value] == value:
            del a_dictionary[value]

    return(a_dictionary)
