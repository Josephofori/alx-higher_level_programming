#!/usr/bin/python3
def no_c(my_string):
    l_string = len(my_string)
    new_string = my_string[:]
    for i in range(l_string):
        if my_string[i] == 'c' or mystring[i] == 'C':
            del my_string[i]
            new_string = my_string.append()
        else:
            new_string = my_string.append()
    print(my_string)
