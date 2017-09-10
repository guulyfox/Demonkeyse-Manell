#!/bin/bash
trap "echo 'I am busy'" 9 5 2 15
n=1
while :
	do
		echo $((n++))
		sleep 1
done
