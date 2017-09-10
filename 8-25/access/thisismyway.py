#!/usr/bin/python3 
import re
with open('access_log','r') as f:
    fead = f.read()
calendar = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

feadout = fead.split("\n")
for i in feadout:
    try:
        go = re.findall("\[.*\]",i)
        gone = go[0]
    except IndexError:
        print("all split work has done!")
        print("FGO die die die!")
    filename = re.subn(re.findall('.*/(.*)/.*',gone)[0],calendar[re.findall('.*/(.*)/.*',gone)[0]],gone)[0]
    filenamename = filename.split(" ")
    filenamename = re.subn(':','_',filenamename[0])[0][1:]
    oneoffile = filenamename.split("_") 
    oneoffile = oneoffile[3]+'/'+oneoffile[2]+'/'+oneoffile[1]+'/'+oneoffile[0]
    with open('access-log-%s.tar.gz'%(re.subn('/','',oneoffile[6:])[0]),'a+') as f:
        f.write(i+'\n')
