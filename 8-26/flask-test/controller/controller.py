# -*- coding: utf-8 -*-
__author__ = 'wenyao'

from main import api,db


from common.auth import *
from user_role import *




api.add_resource(Userinfo,'/v1/api/userinfo/')

