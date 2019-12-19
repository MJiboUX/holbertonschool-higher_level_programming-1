#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    # creating an empty hashet
    hashet = dict()
    for i in range(len(my_list)):
        #if it's not in the hashet, it'll be added
        if (my_list[i] not in hashet.keys()):
            hashet[my_list[i]] = my_list[i]
            s += my_list[i]
    return(s)
