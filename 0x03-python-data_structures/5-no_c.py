#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i == 'c' or i == 'C':
            del my_string[i]
    print(my_string)
