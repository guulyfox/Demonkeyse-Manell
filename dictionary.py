#!/usr/bin/python

user_info={'name':'cali','sex':'male','age':20}
for key in sorted(user_info):
    print("key '=>' %s "%(user_info[key]))

user_info1={'name':'cali','sex':'male','age':20}
for i in user_info1.keys():
    print("i '=>' %s"%(user_info1[i]))

user_info2={'name':'cali','sex':'male','age':20}
ks = list(user_info2.keys())
ks.sort()
for key in ks:
    print("key '=>' %s"%(user_info2[key]))
