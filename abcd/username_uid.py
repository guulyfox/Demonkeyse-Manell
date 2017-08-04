#!/usr/bin/python

import subprocess
f_passwd = subprocess.getoutput("cat /etc/passwd")
f_lines = f_passwd.splitlines()
for i in f_lines:
    print ("username is %s , uid is %s"%(i.split(":")[0],i.split(":")[2]))
