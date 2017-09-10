#!/usr/bin/python3
import subprocess
import sys
f = open('/etc/passwd','r')

s=f.read()
f.close()
s=s.split("\n")
q=len(s)
q=q-1

print(q)
sbc=[]
#for i in range(0,q) 
#    sb=i.split(":")[0]
print(type(s))
print(s)
for i in s:
   sb=i.split(":")
   print(sb[0])
   sbc.append(sb[0])
print(sbc)
print(type(sbc))
sbc.pop()
u_name = input("please input username:")
#if u_name in sbc:
   # print("exists.")
#else:
   #print("not exists.")
for i in sbc:
    if i == u_name:
        print("exists")
        break
    else:
        print("not exists")
        break
