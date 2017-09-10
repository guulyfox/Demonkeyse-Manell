#!/usr/bin/python3

import sys
def aa(x):
    res = [ i*4 for i in x ]
    return res

u_name = sys.argv[1]
map(aa,"cali")
aa("cali")
print(list(map(aa, u_name)))
