#!/usr/bin/python
aa = input("please input something:")
if aa.isdigit():
    
    if int(aa) in [0-100] :
        print ("good input")
    else:
        print ("bad input, please input number in range of 0 to 100.")
else:
    print ("please use numberic.")
