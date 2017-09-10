#!/usr/bin/python3
import os
import subprocess
import shutil
os.system("touch ifcfg-ens33.bak")
ip = input("please input ip:")
netmask = input("please input netmask:")
gateway = input("please input gateway:")
dns = input("please input dns:")
f = open("ifcfg-ens33.bak","r+")
f.write("DEVICE=ens33\nONBOOT=yes\nBOOTPROTO=none\nIPADDR=%s" % (ip))
f.write("\nNETMASK=%s" % (netmask))
f.write("\nGATEWAY=%s" % (gateway))
f.write("\nDNS1=%s\n" % (dns))
f.flush()
f.close()
os.system("mv ifcfg-ens33.bak /etc/sysconfig/network-scripts/ifcfg-ens33")
os.system("service network restart")
