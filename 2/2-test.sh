#!/bin/bash
echo "####################"
count=(`cat xferlog|awk '{print $7}'|sort|uniq -c|sort -rn|awk '{print $1}'`)
ipaddr=(`cat xferlog|awk '{print $7}'|sort|uniq -c|sort -rn|awk '{print $2}'`)
for i in {0..4}
do
echo "$(($i+1)) ip:${ipaddr[i]} count:${count[i]}"
echo -e  "\n"
done

