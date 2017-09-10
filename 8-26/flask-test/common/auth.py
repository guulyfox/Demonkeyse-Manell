# -*- coding: utf-8 -*-
__author__ = 'wenyao'

import sys
sys.path.append('..')

from conf.config import *
#import requests
from flask import request,redirect,g,session,make_response,render_template,abort,current_app
import datetime,time
from main import app
from model.model import *

import hashlib
import hmac
import base64
import urllib
import  uuid


def check_user(args):
    username = args['username']
    user = User_auth.query.filter_by(user_name=username).first()
    if user:
        if user.user_passwd == args['user_password']:
            session['username'] = user.user_name
            session['userid'] = user.id
            return True
    return False

def get_session_sign(session,key):
    sort_keys = session.keys()
    sort_keys.sort()
    sign_str = ''
    sign_dict = {}
    for k in sort_keys:
        sign_str += str(k) + str(session[k])
        sign_dict[k] = session[k]
    md5 = hashlib.md5()
    md5.update(key)
    md5.update(sign_str)
    sign_dict['sign'] = md5.hexdigest()
    return sign_dict



@app.route('/v1/api/auth/',methods=['GET'])
def authentication():
    args = request.args

    if check_user(args):
        sessionid = str(uuid.uuid4())
        session['sessionid'] = sessionid
        current_app.memcache.set(sessionid,get_session_sign(session,SECRET_KEY),time=10)
        response = make_response()
        response.set_cookie('sessionid', sessionid)

        return response

