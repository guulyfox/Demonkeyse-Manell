#!/usr/bin/python
import os
way = input("plwase input the path:")
py_list=[]
for path, d_name, f_name in os.walk(way):
    for i in f_name:
        if i.endswith(".py"):
            print(os.path.join(path, i))
            py_list.append(os.path.join(path,i))

print(len(py_list))
