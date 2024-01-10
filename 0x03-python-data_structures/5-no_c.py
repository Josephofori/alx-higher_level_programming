#!/usr/bin/python3
def no_c(my_string):
    l_string = len(my_string)
    new_string = list(my_string)
    string_update = []
    for i in range(l_string):
        if new_string[i] == 'c' or new_string[i] == 'C':
            del new_string[i]
        else:
            string_update = new_string.append(new_string[i])
    print(string_update)
