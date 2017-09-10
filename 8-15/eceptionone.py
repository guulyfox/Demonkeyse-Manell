#!/usr/bin/python3

try:
    meinv =zhaoliying
    f = open("daydayuptxt","w+")
    f = open("daydayup2.txt","r+")
    f.write("guuly python Manell")
    f.close()
except NameError as e:
    print(e)
    print("please try another.") 
except FileNotFoundError:
    print("file was not exists")
else: 
    print("ok")
