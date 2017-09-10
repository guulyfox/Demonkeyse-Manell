#!/usr/bin/python
import pdb
str = "****feng**8*c*ali***sanle**zhaoli*yi*ng*"
g_str = ''.join(str.split("*"))
pdb.set_trace
num = str.count("*")*'*'
print(num+g_str)
