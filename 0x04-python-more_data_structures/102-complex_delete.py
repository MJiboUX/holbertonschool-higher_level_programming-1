#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # if value in a_dictionary:
    #    del(a_dictionary[value])
    # return(a_dictionary)

    for k, v in enumerate(a_dictionary):
        if v == value:
            del(a_dictionary[k])
    return(a_dictionary)
