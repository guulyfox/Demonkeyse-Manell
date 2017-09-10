#!/usr/bin/python3
import re
'''1'''
def one():
    print("*"*10)
    f = open("passwd")
    fr = f.read()

    p = re.compile('.*sbin.*\n')

    pr = p.findall(fr)
    print(pr,sep="")
    print(len(pr))
    print("*"*10)

'''2'''
def two():
    print("*"*10)
    f = open("passwd")
    fr = f.read()

    p = re.compile('(?P<unm>\w+):\w:(?P<uid>[0-9]{3}):.*\n')
    pr = p.findall(fr)
    print(pr)
    print("*"*10)

'''3'''
def three():
    print("*"*10)
    f = open("passwd")
    fr = f.read()
    
    p = re.compile(r'.*feng.*:x:\d{4}:.*bash\n')
    pr = p.findall(fr)
    print(pr)
    print("*"*10)

'''4'''
def four():
    print("*"*10)
    f = open("passwd","w+")
    fr = f.read()
    
    p = re.compile(r'.*:sbin:.*\n')
    pr = p.sub('cali',fr)
    f.write(pr)
    f.close()
    print(pr)
    print("*"*10)


four()
