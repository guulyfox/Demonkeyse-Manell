#!/bin/bash
username=(`cat /etc/passwd |awk -F: '{if($3>=500&&$3<=5000)print $1,$3,$4,$6,$7}'|awk '{print $1}'`)
uid=(`cat /etc/passwd |awk -F: '{if($3>=500&&$3<=5000)print $1,$3,$4,$6,$7}'|awk '{print $2}'`)
gid=(`cat /etc/passwd |awk -F: '{if($3>=500&&$3<=5000)print $1,$3,$4,$6,$7}'|awk '{print $3}'`)

count=$((${#username[@]}-1))

#echo "$count"

for i in `seq 0 $count`
do
	echo "username ${username[i]} uid ${uid[i]} gid ${gid[i]}"
done
