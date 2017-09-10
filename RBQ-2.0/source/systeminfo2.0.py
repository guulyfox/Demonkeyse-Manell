#!/usr/bin/python
import psutil
import time
# menu
def menu():
    # let user to choose fuction they like
    print("**10")
    print("1 cpu check" )
    print("2 memory check")
    print("3 network check")
    print("4 disk check")
    print("**10")
    choose = input("please let me know what you want to do? choice:")
    choice = ['1','2','3','4']
    if choose in choice:
        return choose
    else:
        print("Let me think")
        time.sleep(1)
        print("we couldn't find any useful messages!")
        return('0')



def diskinfo():
    # monitor disk information (include mount dsetionation and usages and speed )
    disk_partitions = psutil.disk_partitions()
    d = []
    f = 1
    print("mount information" )
    for i in disk_partitions:
        c = i
        d.append(c[1])
    for j in d:
            print("%d. (%s) mount site. total=%d , used=%d  ,free=%d  ,precent=%f %% ."%(f,j,psutil.disk_usage(j)[0],psutil.disk_usage(j)[1],psutil.disk_usage(j)[2],psutil.disk_usage(j)[3]))
            f += 1
    disk_io_counters = psutil.disk_io_counters()
    print("\n")
    print("disk I/O information")
    print("read_count= %d, write_count= %d, reaad_bytes= %d, write_bytes= %d, read_time= %d, write_time= %d, busy_time= %d"%(disk_io_counters[0],disk_io_counters[1],disk_io_counters[2],disk_io_counters[3],disk_io_counters[4],disk_io_counters[5],disk_io_counters[8]))
    

def memoryinfo():
    #monitor memory informatiuon (include usages and total physical size)
    print("memory information:")
    virtual_memory = psutil.virtual_memory()
    print("total= %d M, available= %d M, percent= %d %% ."%(virtual_memory[0]/1024//1024, virtual_memory[1]/1024//1024, virtual_memory[2]))
    print("free= %d M, actice= %d M, inactive= %d M ."%(virtual_memory[3]/1024//1024, virtual_memory[4]/1024//1024, virtual_memory[5]/1024//1024))
    print("\n")

def networkinfo():
    # monitor network info (include send and riceved amount, packages, etc... )
    print("network ip and so on:")
    print("\n")
    interface = list(psutil.net_if_addrs())
    addrs = psutil.net_if_addrs()
    for i in interface:
        print(i,*addrs[i])
        print("\n")
    print("\n")
    net_io_counters = psutil.net_io_counters()
    print("network informations")
    print("bytes_sent= %d b, bytes_recv= %d b, packets_sent= %d , packets_recv= %d ."%(net_io_counters[0],net_io_counters[1],net_io_counters[2],net_io_counters[3])) 

def cpuinfo():
    # monitor cpu usage (include cpu usage and system operating time s )
    cpu_times_percent = psutil.cpu_times_percent()
    print("cpu data for now :")
    print("cpu-forward:   user= %f %%, nice= %f %%, system=%f %%." %(cpu_times_percent[0],cpu_times_percent[1],cpu_times_percent[2]))
    print("cpu-afterward: idel= %f %%, iowait= %f %%, steal= %f %%."%(cpu_times_percent[3],cpu_times_percent[4],cpu_times_percent[7]))
    print("-----------end-----------")


key = {'1':cpuinfo, '2':memoryinfo, '3':networkinfo, '4':diskinfo}

def main():
    # a main function to run all moude
    while True:
        opt = menu()
        if opt in key:
           key.get(opt)()
        else:
           break
    # how to write a dictionary??
    #diskinfo()
    #memoryinfo()
    #networkinfo()
    #cpuinfo()
main()
