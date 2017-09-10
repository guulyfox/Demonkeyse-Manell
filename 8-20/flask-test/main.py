# -*- coding: utf-8 -*-
__author__ = 'wenyao'
import sys
from app.app import APP
from conf import config
from conf.config import *
from flask import abort,request,current_app,make_response,jsonify
from functools import wraps
import time
import socket
import hashlib
import json
import datetime
import logging



app = APP(config)

db = app.get_db()
api = app.get_api()


from controller import controller
