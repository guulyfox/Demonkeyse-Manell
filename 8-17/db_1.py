#!/usr/bin/env python3

import pymysql as mysqldb
#connece to database
db = mysqldb.connect(user="root", passwd="", host="localhost")
db.autocommit(True)
cursor = db.cursor()
c_db = "create database sanle_3"
cursor.execute(c_db)
c_tb = "create table sanle_3.student(id int , name varchar(10), age int ,phonenum decimal(20), address varchar(60), major varchar(20), primary key(id))"
cursor.execute(c_tb)
i_data = "insert into sanle_3.student(id,name,age,phonenum,address,major) values (5,'aali',33,18908495097,'yougzhou','computer science')"
cursor.execute(i_data)

#insert 3 record data tp table
rose_num = 18012345687
rose_add = 'changde'
rose_major = 'English'

rose_data = "insert into sanle_3.student (id,name,age,phonenum,address,major)values(8,'rose',13,'{num}','{add}','{major}')".format(num=rose_num, add=rose_add, major=rose_major)
cursor.execute(rose_data)

s_sql = "select * from sanle_3.student"
cursor.execute(s_sql)
for i in cursor.fetchall():
    print(i)
