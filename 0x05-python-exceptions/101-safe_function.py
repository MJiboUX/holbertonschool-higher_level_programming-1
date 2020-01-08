#!/usr/bin/python3
import sys from stderr


def safe_function(fct, *args):
    try:
        return(fct(*args))
    except Exception as ex:
        print("Exeption: {}".format(ex), file=stderr)
        return(None)
