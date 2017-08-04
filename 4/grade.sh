#!/bin/bash
read -p "please input grade: " _grade
if echo $_grade |egrep -v "([0-9]|[1-9][0-9])" &>/dev/null
then	
	echo "input error,please input number at range in 0 to 100"
else
	echo "good"
	
	if (($_grade>=90&&$_grade<=100))
	then
		echo "good job, may be you can try join alibaba"
	elif (($_grade>=80&&$_grade<90))
	then
		echo "nice, may be you can try join tencent"
	elif (($_grade>=60&&$_grade<80))
	then
		echo "come on, baby! may be you can join facebook"
	else 
		echo "keep on fighting, may be you can try join google"
	fi

	
fi
