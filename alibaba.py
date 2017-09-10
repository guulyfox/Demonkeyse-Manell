#!/usr/bin/python

str = "****feng**8*c*ali***sanle**zhaoli*yi*ng*"
g_str = ''.join(str.split("*"))

num = str.count("*")*'*'
print(num+g_str)
