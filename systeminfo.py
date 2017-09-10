#!/usr/bin/python3
import psutil
print("system info monitor")
a = ['cpu','memory','disk','network']
b = [psutil.cpu_stats(), psutil.virtual_memory(), psutil.disk_usage("/"), psutil.net_if_stats()]
c = dict(zip(a,b))
print(c)
print("\n" )
for i in a:
   print(i)
   print(c[i], sep="\n")
   print("\n")
