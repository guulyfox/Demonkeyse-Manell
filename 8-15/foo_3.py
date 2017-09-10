#!/usr/bin/python3
import logging
def use_logging(func):


    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args)
    return wrapper

@use_logging
def foo():
    print("I am foo")

@use_logging
def bar():
    print("I am bar")



foo()

bar()
