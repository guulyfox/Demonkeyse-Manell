#!/bin/bash
menu(){
	echo -e "###############"
	echo -e "1, add user "
	echo -e "2, delete user "
	echo -e "3, query user information "
	echo -e "4, reset user's password "
	echo -e "5, modify user's information "
	echo -e "6, exit"
	echo -e "###############"
	echo 
	read -p "please input your option " _option
}
	
modify(){
	
	echo -e "##############"
	echo -e "1, change user's uid " 
	echo -e "2, change user's gid " 
	echo -e "3, change user's shell " 
	echo -e "4, change user's home " 
	echo -e "##############"
	echo -e "press other key to return"
	echo -e "##############"
	read -p "please input your choice " _choice
		
while :
do
	case $_choice in
	1)
		read -p "please input user's uid " _uid	
		if echo "$_uid"|egrep "[0-9]+"
		then
			usermod -u $_uid $_musername
			main
		else
			echo "input ilegal"
			modify
		fi
	;;
	2)
		read -p "please input user's gid " _gid
		if echo "$_gid"|egrep "[0-9]+"
		then
			usermod -g $_gid $_musername
			main
		else
			echo "input ilegal"
			modify
		fi		
	;;
	3)
		read -p "please input user's shell " _shell
		if echo "$_shell"|grep "`cat /etc/passwd|awk '{print $7}'`"
		then
			usermod -s $_shell $_musername
			main
		else
			echo "not found! "
			modify
		fi
	;;
	4)
		read -p "please input user's home" _home
		if echo "$_home"|grep "`cat /etc/passwd|awk '{print $6}'`"
		then
			usermod -d $_home $_musername
			main
		else
			echo "please not touble toubles!"
			modify
		fi
	;;
	*)
		main
	;;
	esac
done
}




main(){
while :
do
	menu
	case $_option in
	1)
	read -p "please input your user's name: " _uname
	if cat /etc/passwd|egrep "^$_uname"
	then
		echo "already exist, try another "
		main
	else
		useradd $_uname
		read -p "please input your user's passwd: " _passwd
		echo "$_passwd"|passwd --stdin $_uname
		echo "all changes are done "
	fi
	;;
	2)
	read -p "which user you want to delete " _dname
	if cat /etc/passwd|egrep "^$_dname"
	then
		userdel $_dname
		echo "all changes are done"
	else
		echo "what have you done? no result we found "
	fi
	;;
	3)
	read -p "which users you want to query?" _qname
	if cat /etc/passwd |egrep "^$_qname"
	then
		cat /etc/passwd |grep "$_qname" |awk -F: '{print $1,$3,$4,$6,$7}'
	else
		echo "no results but our chickens "
		main
	fi
	;;
	4)
	read -p "which users you want to reset passwd? " _pname
	if cat /etc/passwd |egrep "^$_pname"
	then
		read -p "please input password you want to reset " _npasswd
		echo "$_npasswd"|passwd --stdin $_pname
	else
		"no result but our RBQs"
		main
	fi
	;;
	5)
	 read -p "please input a username that you want to modify " _musername
        if echo "$_musername"|egrep "^$_musername"
        then
		modify
	else
		echo "see RBQs"
	fi
	;;
	6)
	exit
	;;
	*)
	exit
	;;	

	esac
done
}
main
