#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        q = a / b
        return(a / b)
    except ZeroDivisionError:
        q = None
        return(None)
    finally:
        print("Inside result: {}".format(q))
