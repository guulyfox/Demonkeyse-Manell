#! /usr/bin/python
import time
import pymysql
import re
import shutil
import psutil

'''how to write data to db?'''
def main():
    flag = 1

    db = pymysql.connect(user = "root", passwd = "", host = "localhost")
    '''to create a free memory to tempory locate data'''
    cursor = db.cursor()
    SHDB ="show databases"
    cursor.execute(SHDB)
    Tu_DB  = cursor.fetchall()

    '''find a paticularly database in databases'''
    for i in Tu_DB:
        j = list(i)[0]
        if j == 'lolita':
            flag = 0

    '''if lolita exists, then do not to create it to make a error'''
    if flag:
        cre_DB = "create database lolita"
        cursor.execute(cre_DB)

    use_DB = "use lolita"
    cursor.execute(use_DB)
    SH_TB = "show tables"
    cursor.execute(SH_TB)
    RE_SH_TB = cursor.fetchall()


    '''init flag'''
    flag = 1
    '''find a paticularly table in tables'''
    for i in RE_SH_TB:
        j = list(i)[0]
        if j == 'loli':
            flag = 0

    '''if table loli exists, then do not to create the same one'''
    if flag:
        cre_tb = "create table loli(time varchar(30), sent_all int, recv_all int, primary key (time))"
        cursor.execute(cre_tb)



    '''lolita'''
    a = 0
    b = 0
    a = psutil.net_io_counters().bytes_sent
    b = psutil.net_io_counters().bytes_recv
    while True:
        a1 = psutil.net_io_counters().bytes_sent
        b1 = psutil.net_io_counters().bytes_recv
        sent_all = a1 - a
        recv_all = b1 - b
        a = a1
        b = b1
        ctime = time.ctime()
        print ("%s  s:%d  r:%d" %(ctime, sent_all, recv_all))
        insert_into = "insert into loli(time, sent_all, recv_all) values ('{time}', {sent}, {recv})".format(time=ctime , sent=sent_all, recv=recv_all)
        cursor.execute(insert_into)
        try:
            db.commit()
        except:
            db.rollback()
        time.sleep(1)
    '''lolita'''


    '''use time or ctime'''
if not '__name__' == '__main__':
    main()

