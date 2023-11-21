#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        num = fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        num = None
    return (num)
