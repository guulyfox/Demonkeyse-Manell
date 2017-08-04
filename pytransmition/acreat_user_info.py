#!/usr/bin/python3
u_name = input ("please input your name: ")
u_pwd = input ("please input your password: ")

print ("your name is %s your password is %s" % (u_name,u_pwd))
# compare the length of password
if len(u_pwd) < 6 :
   print ("your password is too short, just have % d"% len(u_pwd))
elif len(u_pwd) == 6 :
   print ("it's ok of your password length")
else :
   print ("it's strong of your password length")
