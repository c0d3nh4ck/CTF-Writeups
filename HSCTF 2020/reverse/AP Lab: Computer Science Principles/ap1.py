#!/usr/bin/python
def rev_shift(input):
    rev = ""
    for i in range(len(input)):
        rev += chr(ord(input[i])+i)
    print rev

def rev_shift2(input):
    rev = ""
    for i in range(len(input)):
        rev += chr( ord(input[i]) - len(str(ord(input[i]))) )

    return rev

rev_shift(rev_shift2("inagzgkpm)Wl&Tg&io"))