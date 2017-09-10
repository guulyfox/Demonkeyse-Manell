# -*- coding: utf-8 -*-

__author__ = 'wenyao'

import sys
sys.path.append('..')

from main import db


from sqlalchemy import Column, Integer, DateTime
import datetime,time


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String)
    user_sex = db.Column(db.String)
    user_age = db.Column(db.Integer)
    user_phone = db.Column(db.String)
    user_addr = db.Column(db.String,default='xxx')

    def __init__(self,user_name,user_sex,user_age,user_phone,user_addr):
        self.user_name = user_name
        self.user_sex = user_sex
        self.user_age = user_age
        self.user_phone = user_phone
        self.user_addr = user_addr

    def to_json(self):
        return {
            "user_name":self.user_name,
            "user_sex":self.user_sex,
            "user_age":self.user_age,
            "user_phone":self.user_phone,
            "user_addr":self.user_addr
        }

class User_auth(db.Model):
    __tablename__ = 'User_auth'
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String)
    user_passwd = db.Column(db.String)

    def __init__(self,user_name,user_passwd):
        self.user_name = user_name
        self.user_passwd = user_passwd
