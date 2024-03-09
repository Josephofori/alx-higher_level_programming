#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    denum = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        denum += tup[1]

    return (num / denum)
