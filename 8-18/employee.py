#!/usr/bin/python3

class Employee:
    '''all employee'''
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Emplyee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:%s Salary:%d" % (self.name, self.salary))
