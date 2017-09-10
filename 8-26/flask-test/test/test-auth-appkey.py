#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wenyao'

import hashlib
import hmac
import datetime
import json
import urllib
import urllib2
import time
import requests

appname='flask-test'
appkey='testttttt'


def gen_signature(appkey,http_method,url,timestamp):

    signed_str = appkey + str(timestamp) + http_method + url
    server_sign = hashlib.md5(signed_str).hexdigest()
    return (server_sign,signed_str)

auth_url = "/v1/api/userinfo/"
timestamp = int(time.time())

(sign_key,sign_str) = gen_signature(appkey,"GET",auth_url,timestamp)
param = {'appname':appname,'signature':sign_key,'timestamp':timestamp,'user_id':6}
exec_url='http://192.168.160.130:5000/v1/api/userinfo/?'+ urllib.urlencode(param)
response = requests.get(exec_url)
data = json.loads(response.text)
print data