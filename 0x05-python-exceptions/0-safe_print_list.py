#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        for i in my_list:
            if a <= x - 1:
                print("{}".format(i), end="")
                a += 1
        print()
        return(a)
    except:
        a = 0
        for i in my_list:
            print("{}".format(i), end="")
            a += 1
        print()
        return(a)
