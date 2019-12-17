#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return(None)
    length = len(sentence)
    first = sentence[0:1]
    tuple_s = (length, first)
    return(tuple_s)
