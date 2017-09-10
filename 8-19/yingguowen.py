#!/usr/bin/python3
import psutil
import pymysql
import time 

try :
    db = pymysql.connect(user = "root", passwd = "123123", host = "localhost")
    cursor = db.cursor()
    db.autocommmit(True)
except:
    print("can't connect mysql, please check the username or passwd ")
    exit()

pl_recv = 0
p1_sent = 0
b1_recv = 0
b1_sent = 0
flag = 0

i = 0

while True:
   p2_recv = psutil.net_io_counters().packets_recv
   p2_sent = psutil.net_io_counters().packets_sent
   b2_recv = psutil.net_io_counters().bytes_recv
   b2_recv = 
