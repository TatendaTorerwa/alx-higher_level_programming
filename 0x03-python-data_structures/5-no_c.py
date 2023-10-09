#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for p in my_string:
        if p == "c" or p == "C":
            continue
        result += p
    return result
