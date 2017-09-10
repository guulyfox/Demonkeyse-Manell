#!/usr/bin/python
import time
import os
import shutil
try:
   f = open("/python/aa.txt","a+")
   aa = input("please input something:\n")
   f.write(aa)
   f.flush()
   f.close()
except Exception as e:
   f = open("/python/aa_log.txt","a+")
   utime = time.ctime()
   uname = os.getlogin()
   content = e
   f.write(str(e)+":"+utime+":"+uname+":"+aa+"\n")
   f.flush()
   f.close()
