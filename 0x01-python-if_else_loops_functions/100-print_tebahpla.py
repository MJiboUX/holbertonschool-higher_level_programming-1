#!/usr/bin/python3
for i in range(122, 96, -1):
    a = i
    if a % 2 != 0:
        a = a - 32
    print("{}".format(chr(a)), end="")
