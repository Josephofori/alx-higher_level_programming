#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        num = fct(*args)
    except Exception as err:
        sys.sderr.write("Exception: {}\n".format(err))
        num = None
    return (num)
