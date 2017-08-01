#!/bin/bash
cat web.log |egrep -o "[a-Z]+\.[0-Z]+\.[a-Z]+" --color|sort|uniq -c|sort -rn
