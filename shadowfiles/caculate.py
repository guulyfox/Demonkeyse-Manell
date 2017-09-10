#! /usr/bin/python3
num = input ("please input two numbers:")
num1 = num.split(" ")
print("%d * %d = %d"%(int(num1[0]),int(num1[1]),(int(num1[0]) * int(num1[1]))))
print("%d - %d = %d"%(int(num1[0]),int(num1[1]),(int(num1[0]) - int(num1[1]))))
print("%d / %d = %d"%(int(num1[0]),int(num1[1]),(int(num1[0]) / int(num1[1]))))
print("%d ** %d = %d"%(int(num1[0]),int(num1[1]),(int(num1[0]) ** int(num1[1]))))
print("%d // %d = %d"%(int(num1[0]),int(num1[1]),(int(num1[0]) // int(num1[1]))))
print("%d %% %d = %d"%(int(num1[0]),int(num1[1]),(int(num1[0]) % int(num1[1]))))
