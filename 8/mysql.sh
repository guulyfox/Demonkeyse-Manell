#!/bin/bash
menu()
{
	echo -e "\e[31mhello, do you want to create a database? \e[0m"
	echo -e "\e[65m1, create a database sanle named sanle \e[0m"
	echo -e "\e[13m2, insert datas in sanle \e[0m"
	echo -e "\e[90m3, query information of sanle \e[0m"
	read -p "please input your choice: " _chioce
}

main(){
while :
do
clear




	


menu
case $_chioce in
	1)
	echo "yes I working on it,please wait"
	mysql<<EOF
show databases;
create database sanle;
show databases;

EOF
	read
	clear
	;;
	2)
	echo "ok show me what you want"
	mysql<<EOF
show databases;
use sanle;
show tables;
create table student(student_id int primary key,student_name varchar(20),student_sex varchar(10),student_address varchar(30),student_phone int,student_grade int);

EOF
echo "now you must input message!"
for i in {0..3} 
do

read -p "insert student's id, name, sex, address, phone number, grade: " a b c d e f
 
	mysql<<EOF
show databases;
use sanle;
show tables;
insert into student(student_id,student_name,student_sex,student_address,student_phone,student_grade)values($a,'$b','$c','$d',$e,$f);
use sanle;
select * from student;

EOF
done
	read
	clear
	;;
	3)
	echo "here's imformations here"
	mysql<<EOF
	use sanle;
	select * from student;
	
EOF
	read
	clear
	;;
	*)
	exit
	;;
esac
done
}
main
