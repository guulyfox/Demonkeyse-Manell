#!/usr/bin/python3
import os
import time
import logging



def socketer(func):
    
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        print(args[0],args[1])  
        base = check(args[0],args[1])
        return func(*args, **kwargs)


    return wrapper


def menu():
    u_name = input("please input user's name that you want to create:")
    u_passwd = input("please input your passwd for this user:")
    return(u_name,u_passwd)


@socketer
def create(u_name,u_passwd):

    os.system("useradd %s" % u_name) 
    os.system("echo %s |passwd --stdin %s" % (u_passwd, u_name))
    print("ganurate a user complete!")


def check(a,b):
    
    if not os.system("id %s " % a) == 0:

        if bool(os.system('echo %s |egrep "[0-9]"|egrep "[A-Z]"|egrep "[^0-Z]"|egrep "[a-z]" ' % b) == 0):
        
            pass 

        else:
            print("your passwd is to simply, please make sure contain numbers and upper and lower alpha and special characters!")
            raise TypeError  
    else:
        print("this user has already exist!")
        raise TypeError

def main():

   try:     
        a,b= menu()
        create(a,b)

   expect:

main()
