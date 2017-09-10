# -*- coding: utf-8 -*-
__author__ = 'wenyao'
import sys
from app.app import APP
from conf import config

from conf.config import *
from flask import abort,request,current_app,make_response,jsonify
from functools import wraps
import time
import memcache
#from common.auth import get_session_sign

import socket
import hashlib
import json
import datetime
import logging


reload(sys)
sys.setdefaultencoding('utf-8')

app = APP(config)


db = app.get_db()
api = app.get_api()
app.db = db

mc = memcache.Client(config.memcache_servers)
app.memcache = mc


class appKey(db.Model):
    __tablename__ = 'app_key'
    id = db.Column(db.Integer,primary_key=True)
    appname = db.Column(db.String)
    appkey = db.Column(db.String)
    owner = db.Column(db.String)
    expire_time = db.Column(db.Date)
    apply_time = db.Column(db.Date)

    def __init__(self, appname, appkey, expire, apply_time, owner):
        self.appname = appname
        self.appkey = appkey
        self.expire = expire
        self.apply_time = apply_time
        self.owner = owner

    def to_json(self):
        return {
            "appname":self.appname,
            "appkey":self.appkey,
            "expire":str(self.expire),
            "apply_time":str(self.apply_time),
            "owner":self.owner,
        }

def auth_required():
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if current_app.config['LOGIN_DISABLED']:
                resp = func(*args, **kwargs)
            else:
                if session_auth():
                    pass
                elif app_key_auth():
                    pass
                else:
                    abort(401)
                resp = func(*args, **kwargs)
            response = make_response(resp)
            return response
        return decorated_view
    return wrapper


def session_auth():
    '''
    Use Memcached store session info, ttl to expire
    key: sessionid
    '''
    sessionid = str(request.cookies.get('sessionid'))
    if sessionid:
        sessioninfo = current_app.memcache.get(sessionid)
        if sessioninfo:
            #current_app.logger.debug(type(sessioninfo))
            if sessioninfo:
                return True
    return False

def app_key_auth():
    '''
    md5(lower(appkey + timestamp + http_method + url + params))
    example : POST http://domain/v1/api/xxx?name=a&age=12  {'param1':124,'parm2':'xxxx'}
    url = /v1/api/xxx?name=a&agen=12
    http_method = POST
    timestamp = int(time.time())
    '''
    appname = request.args.get('appname')
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    url = request.path
    http_method = request.method
    print url,appname

    if check_signature(appname=appname, timestamp=timestamp, http_method=http_method, url=url, signature=signature):
        return True
    return False

def check_signature(appname,timestamp,http_method,url,signature):
    current_app.logger.debug('appkey auth start.....')
    appkey_info = appKey.query.filter_by(appname=appname).first()
    if not appkey_info:
        return False
    if not signature or not timestamp:
        return False

    appkey = appkey_info.appkey
    signed_str = appkey + str(timestamp) + http_method + url
    server_sign = hashlib.md5(signed_str).hexdigest()
    if signature.startswith(server_sign):
        return True
    else:
        return False


api.decorators.append(auth_required())

from controller import controller
