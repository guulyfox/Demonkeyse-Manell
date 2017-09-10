import psutil
import time
import pymysql as mysqldb

db = mysqldb.connect(user='root', passwd="", db="python", host="localhost")
db.autocommit(True)
cur = db.cursor()
def sys_netinfo(bytes_sent_all_old, bytes_recv_all_old):
    sys_netio_all = psutil.net_io_counters()
    global bytes_sent_all
    global bytes_recv_all
    bytes_sent_all = sys_netio_all.bytes_sent
    bytes_recv_all = sys_netio_all.bytes_recv
    bytes_sent = sys_netio_all.bytes_sent - bytes_sent_all_old
    bytes_recv = sys_netio_all.bytes_recv - bytes_recv_all_old
    return bytes_sent, bytes_recv

bytes_sent_all = 0
bytes_recv_all = 0
first_flag = 1

if __name__ == "__main__":
    while True:
        bytes_sent, bytes_recv = sys_netinfo(bytes_sent_all, bytes_recv_all)
        timestamp = int(time.time())
        if first_flag:
            first_flag = 0
            continue
        print(timestamp, bytes_sent, bytes_recv)
        sql = "insert into nic(time, nic_in, nic_out) values({timestamp},{bytes_recv},{bytes_sent})".format(timestamp=timestamp, bytes_recv=bytes_recv, bytes_sent=bytes_sent)
        cur.execute(sql)
        time.sleep(1)
