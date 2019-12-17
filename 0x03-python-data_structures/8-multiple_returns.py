#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        return(length, None)
    first = sentence[0:1]
    tuple_s = (length, first)
    return(tuple_s)
