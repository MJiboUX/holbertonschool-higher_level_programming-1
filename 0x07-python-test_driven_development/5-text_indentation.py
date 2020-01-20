#!/usr/bin/python3
"""
text indentation function
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of ".", "?" and ":"
       Args:
           text: the text that will be printed with the new lines.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = list(text)
    for i in range(len(s)):
        if s[i] == ".":
            s[i] = ".\n\n"
            if s[i+1] == " ":
                s[i+1] = ""
        if s[i] == ":":
            s[i] = ":\n\n"
            if s[i+1] == " ":
                s[i+1] = ""
        if s[i] == "?":
            s[i] = "?\n\n"
            if s[i+1] == " ":
                s[i+1] = ""
    nospace = ""
    nospace = nospace.join(s)
    print(nospace, end="")
