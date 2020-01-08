#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l = []
    try:
        for i in range(list_length):
            l.append(my_list_1[i] / my_list_2[i])
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return(l)
