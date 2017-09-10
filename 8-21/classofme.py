#!/usr/bin/python3

class school_member:
    def __init__ (self, name, sex, age, address):
         self.name = name
         self.sex = sex
         self.age = age
         self.address = address
         instct.count += 1
    def howmany(self):
         return instct.count

    def displayall(self):
         print("name: {0}, sex: {1}, age: {2}, address: {3}".format(self.name, self.sex, self.age, self.address))

class school_student (school_member):
    def prt(self):
         print("student")
         displayall(self)

class school_teacher (school_member):
    def prt(self):
        print("teacher")
        displayall(self)

if __name__ == "__main__":
    print("Do not use it directly!")
