#!/usr/bin/python3
score = input("please input your grade:")
if score.isdigit():
    if 90 <= int(score) <= 100:
        print("A")
    elif 80 <= int(score) < 90:
        print("B")
    elif 70 <= int(score) < 80:
        print("C")
    elif int(score)<70:
        print("D")
    else:
        print("out of range")
else:
    print("please input a number")
