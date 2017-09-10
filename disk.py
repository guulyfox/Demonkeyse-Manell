#!/usr/bin/python3
import os

os.system("df -h |awk '{print $6}'|head -8|tail -7  &>a.txt")
os.system("df -h |awk '{print $5}'|head -8|tail -7  &>b.txt")
a=[]
b=[]
d = os.popen("cat /8-3/a.txt").readlines()
f = os.popen("cat /8-3/b.txt").readlines()
print(d)

print(f)

for i in d:
   a=a+i.split("\n")
print(a)


for i in f:
   b=b+i.split("\n")
print(b)
print("###################")
print(str(a))
print(str(b))
print("###################")
aa = str(a).split("\n")[0]
bb = str(b).split("\n")[0]
print(aa)
print(bb)
print("\n")
disk=dict(zip(a,b))
print('disk')
print(disk)
print("\n")

z = open('/8-3/a.txt','r')
zz = [x.split('\n')[0] for x in z]
z.close()
print(zz)

v = open('/8-3/b.txt','r')
vv = [x.split('\n')[0] for x in v]
v.close()
print(vv)
print("\n")
disk2=dict(zip(a,b))
print('disk2')
print(disk)
print("\n")
