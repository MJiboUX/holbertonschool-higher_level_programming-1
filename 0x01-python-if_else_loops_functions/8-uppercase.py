#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = i
        if ord(i) >= 97 and ord(i) <= 122:
            a = chr(ord(i) - 32)
        print("{}".format(a), end="")
    print("\n", end="")
