#!/usr/bin/python3

import memcache
mc = memcache.Client(['192.168.0.73:11211'],debug=0)
mc.set("foo","bar")
value = mc.get("foo")
print(value)
