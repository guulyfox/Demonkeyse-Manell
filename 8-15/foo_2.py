#!/usr/bin/python3
import logging
def use_logging(func):
   logging.warn("%s is runnung "%func.__name__)
   func()

def bar():
    print('I am bar') 

use_logging(bar) 
