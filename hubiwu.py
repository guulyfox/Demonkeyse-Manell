#! /usr/bin/python

__all__ = ["_private_teacher","public_teacher","public_var"]
public_var = "hello, I am a public variable."
_private_var = "hello. I am a private variable"

def public_teacher():
    print("public teacher cali")

def _private_teacher():
    print("private teacher rose")
