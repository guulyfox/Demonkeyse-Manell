#!/usr/bin/python3

import re

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print ("m.re:", m.re)
print ("m.pos:", m.pos)
print ("m.endpos:", m.endpos)
print ("m.lastindex:", m.lastindex)

print ("m.group(1,2):", m.group(1,2))
print ("m.groups():", m.groups())
print ("m.groupdict:", m.groupdict())
print ("m.start(2):", m.start)
print ("m.end(2):", m.end(2))
print ("m.span(2):", m.span(2))
print (r"m.expand(r'\2 \1\3'):",  m.expand(r'\2 \1\3'))
