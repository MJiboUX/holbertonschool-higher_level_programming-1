#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in my_list:
        if i <= x:
            print("{:d}".format(i), end="")
        else:
            i -= 1
            break
    print()
    return(i)
