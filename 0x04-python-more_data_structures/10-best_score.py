#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return(None)
    best = ""
    score = 0
    for key in a_dictionary:
        if a_dictionary[key] > score:
            best = key
    return(best)
