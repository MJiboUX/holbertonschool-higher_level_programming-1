#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return(0)
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    s = 0
    string = list(roman_string)
    for i, j in roman.items():
        for k in string:
            if i == k:
                s = s + j
    return(s)
