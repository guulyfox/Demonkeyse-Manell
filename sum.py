#!/usr/bin/python

a = 0

def sum(i):
     
    while i:
        global a
         
        print("{}".format(sum(i - 1)))        
 
        return sum(i - 1)
    else:
        print(a)
    

def main():
    i = 10
    a = 0
    sum(i)


main()
