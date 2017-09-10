#!/usr/bin/python3

'''Fibonnacci numbers module'''

def fib(n):
    '''write Fibonacci series up to n'''
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
        return result

fibs = [0, 1]
numZS = int(input('How many Fibonacci numbers do you want?'))

for i in range(numZS-2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)
