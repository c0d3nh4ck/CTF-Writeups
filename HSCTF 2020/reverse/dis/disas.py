#!/usr/bin/python
import dis

def a(s):
    o = [0] * len(s)
    for i,c in enumerate(s):
        o[i] = c * 2 - 60
    return o

def b(s,t):
    for x,y in zip(s,t):
        yield x + y - 50

def j(s): # renaming "c" as "j"
    return [c+5 for c in s]

def e(s):
    s = [ord(c) for c in s]
    o = [(c^5)-30 for c in b(a(s),j(s))] 
    return bytes(o)

def main():
    # s = input("Guess?")
    o = b'\xae\xc0\xa1\xab\xef\x15\xd8\xca\x18\xc6\xab\x17\x93\xa8\x11\xd7\x18\x15\xd7\x17\xbd\x9a\xc0\xe9\x93\x11\xa7\x04\xa1\x1c\x1c\xed'
    # if e(s) == o:
    #     print("Correct!")
    # else:
    #     print("Wrong!")
    #     print(e(s))

    w = 'flag{'
    x = 6

    while x <= len(o):
    	for i in range(0x20, 0x7f):
    		test = w
    		test += chr(i)
    		if e(w) == o[:x]:
    			x += 1
    			w += chr(i)
    			print(w)
    			break


main()
