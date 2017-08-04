#!/bin/bash
menu(){
	echo -e "\e[32minterfece config network status\e[0m"
	echo -e "1, set hostname "
	echo -e "2, set ip "
	echo -e "3, query ip and hostname "
	read -p "please select your option: " _option  
	clear	
}

network(){

#backup id

echo "first, we need to backup"
        if [ -f /lianxi/9/backup-eth0 ]
        then
                echo "hopefully it will work"
        else
                cp /etc/sysconfig/network-scripts/ifcfg-eth0 /lianxi/9/backup-eth0
        fi
#restore good ip	

        if ping -c1 192.168.233.1
        then
                cp -f /etc/sysconfig/network-scripts/ifcfg-eth0 /lianxi/9/backup-eth0
        else
                cat /lianxi/9/backup-eth0 &> /etc/sysconfig/network-scripts/ifcfg-eth0
	service network restart

#if all done then do initalize

		if ping -c1 192.168.233.1
		then 
			echo "do not do something damgerous!"
			exit
		else
			echo "do initalize"
			sed -ri "s/IPADDR=[0-9]+\..*/IPADDR=192.168.233.212/" /etc/sysconfig/network-scripts/ifcfg-eth0
		fi
        fi
        
        read -p "now you must input your ipaddr:xxxx.xxxx.xxxx.xxxx: " _vul
        if echo "$_vul"|egrep "(19[1-9]|2[01][0-9]|22[123])((\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})"
        then
        	sed -ri "s/IPADDR=[0-9]+\..*/IPADDR=$_vul/" /etc/sysconfig/network-scripts/ifcfg-eth0
        	service network restart
  		network      
        else
        	echo "error, you must input legally!"
        	main
        fi
}

main(){
while :
do
	menu
	case $_option in
	1)
	read -p "please input your hostname" _hsnm
	if echo "$_hsnm"|egrep  "[^0-Z]"
	then 
	echo "error, please input legally"
	main
	else
	sudo hostname $_hsnm
	sed -ri "s/HOSTNAME=[0-Z]+\.[0-Z]+/HOSTNAME=${_hsnm}.${_hsnm}domian/" /etc/sysconfig/network
	cat /etc/sysconfig/network
	fi
	;;
	2)
	network
	;;	
	3)
	echo -e "hostname:"
	cat /etc/sysconfig/network|egrep "^HOSTNAME"
	echo -e "ip"
	cat /etc/sysconfig/network-scripts/ifcfg-eth0|egrep "^IPADDR"
	;;
	*)
	
	exit
	;;
	esac
done
}
main
