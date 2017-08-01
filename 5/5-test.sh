#!/bin/bash
main(){
echo -e "\e[32mcreat user by batter-fly\e[0m"
read -p "please input your suffex that you like to use: " _suffex
if [ -z $_suffex ]
then
	echo "error input"
	read
	clear
	main
else
	echo "good"
fi

echo	
read -p "please input the number of user account that you want to create: " _number
if echo $_number|egrep -v  "[0-9]+" 
then
	echo "error input"
	read
	clear
	main
else
	echo "good"
fi
echo
read -p "please input the passwd that you want to give to global users:" _passwd
if [ -z $_passwd ]
then 
	echo "error input"
	read
	clear
	main
else
	echo "good"
fi

echo  "#######################################"
num1=$(($_number-1))
#echo "$num1"
num=(`seq  $_number`)
#echo "${num[1]}"
for i in `seq 0 ${num1}` 
do
	echo "useradd:${_suffex}${num[i]}"
	useradd ${_suffex}${num[i]}
	echo "$_passwd"|passwd --stdin ${_suffex}${num[i]}
done
for i in `seq 0 ${num1}`
do
	echo "user uid gid home bash"
	cat /etc/passwd|egrep "^${_suffex}${num[i]}"|awk -F: '{print $1,$3,$4,$6,$7}'
	echo
done
}
main 
