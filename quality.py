#!/usr/bin/python
a=""
b=""
all="8*cali*china**it*soft*linux*python"
for i in all:
    if i == "*":
        a = a + i
    else
        b = b + i
else
    c = a + b
======================================
all="8*cali*china**it*soft*linux*python"
b=all.join(str.split("*"))
for i in all:
    if i == "*":
       a = a + i
else
    c = a + b

