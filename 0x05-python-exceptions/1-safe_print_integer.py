#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value.is_integer():
            print("{:d}".format(value-1))
            return(True)
    except AttributeError:
        return(False)
