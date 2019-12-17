#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    x = list(tuple_a)
    y = list(tuple_b)

    if len(x) == 0:
        x = (0, 0)
    if len(y) == 0:
        y = (0, 0)
    if len(x) == 1:
        x = (x[0], 0)
    if len(y) == 1:
        y = (y[0], 0)

    tuple_c = (x[0] + y[0], x[1] + y[1])
    return(tuple_c)
