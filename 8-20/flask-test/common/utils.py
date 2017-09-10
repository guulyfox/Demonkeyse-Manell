# -*- coding: utf-8 -*-
__author__ = 'wenyao'

import urllib2
import sys
sys.path.append('..')


class UTIL:
    @staticmethod
    def to_json(status, message, result=None):
        return {'status':status,'message':message, 'result':result}


   


