#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        a = 0
        for i in my_list:
            if a < x:
                try:
                    print("{:d}".format(i), end="")
                    a += 1
                except:
                    pass
        print()
        return(a)
    except:
        a = 0
        for i in my_list:
            try:
                print("{:d}".format(i), end="")
                a += 1
            except:
                pass
        print()
        return(a)
