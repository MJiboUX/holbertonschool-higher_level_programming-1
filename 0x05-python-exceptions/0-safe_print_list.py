#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in my_list:
        if i <= x:
            try:
                print("{}".format(i), end="")
            except:
                print("An exception occurred")
        else:
            i -= 1 
            break
    print()
    return(i)
