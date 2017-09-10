#!/usr/bin/python3
# without using reverse method let list to be reversed.
L = '2 89 78 23 13 12 16 23 56 67 89 90 54 11 18' 
uu = L.split(' ')
print(uu)
q = len(uu) - 1
i = 0
print(q)
print(range(0,q))
for i in range(0,q):
    aa = 0
    m = q - i
    aa = uu[m]
    uu[m] = uu[i]
    uu[i] = aa
    print(i)
print (uu)
