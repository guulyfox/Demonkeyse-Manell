#!/usr/bin/python3
import os
file =os.popen("cat /etc/passwd")
import subprocess
f_file = subprocess.getoutput("cat /etc/passwd")
f_lines = f_file.splitlines()
for i in f_lines:
    if  500 < int(i.split(":")[2]) < 2000:
        print("username is %s, uid is %s"%(i.split(":")[0],i.split(":")[2]))
