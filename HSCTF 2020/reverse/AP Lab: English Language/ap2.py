#!/usr/bin/python
def xor(input):
    ret = ""
    xr = [4,1,3,1,2,1,3,0,1,4,3,1,2,0,1,4,1,2,3,2,1,0,3]

    for i in range(len(input)):
        ret += chr(ord(input[i])^xr[i])
    return ret

def rev_trans(input):
    rex = ""
    trs = [11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9]
    for i in range(23):
        rex += input[trs.index(i)]
    return rex

inp = "1dd3|y_3tttb5g`q]^dhn3j"

for i in range(0,3):
    inp = xor(inp)
    inp = rev_trans(inp)

    print inp
