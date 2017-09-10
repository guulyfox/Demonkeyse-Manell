# -*- coding: utf-8 -*-
__author__ = 'wenyao'


from main import db,app
from model.model import *
from common.utils import *
from flask import request
from common.common_controller import Restapi
from flask_restful import Resource, reqparse, fields, abort, marshal
from paging import paging_warpper

class Userinfo(Restapi):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('user_name',type=str)
        self.reqparse.add_argument('user_sex',type = str,required=True)
        self.reqparse.add_argument('user_age',type = int,required=True)
        self.reqparse.add_argument('user_phone',type = str,required=True)
        self.reqparse.add_argument('user_addr',type = str,required=True)

    def get(self):
        try:
            # user_id = request.args.get('user_id',0,type=int)
            # user_info = UserInfo.query.get(user_id)
            # result = user_info.to_json()
            page = request.args.get('page',type=int)
            maxnum = request.args.get('maxnum', type= int)
            offset = (page - 1) * maxnum
            ads_list = UserInfo.query.order_by(UserInfo.id.desc()).limit(maxnum).offset(offset).all()
            tmp_list = [] 
            for ads in ads_list:
                tmp = {}
                tmp['user_addr'] = ads.user_addr
                tmp['user_age'] = ads.user_age
                tmp['user_name'] = ads.user_name
                tmp['id'] = ads.id
                tmp_list.append(tmp)
                result = tmp_list
            return result
        except Exception,e:
            db.session.rollback()
            return UTIL.to_json(status=1,message='failed',result=str(e))
        finally:
            db.session.close()
        return UTIL.to_json(status=0,message="get data success",result=result)

    def put(self):
        try:
            user_id = request.args.get('user_id',0,type=int)
            args = self.reqparse.parse_args()

            db.session.begin()
            user_info = UserInfo.query.get(user_id)
            user_info.user_sex = args["user_sex"]
            user_info.user_age = args["user_age"]
            user_info.user_phone = args["user_phone"]
            user_info.user_addr = args["user_addr"]
            db.session.add(user_info)
            db.session.commit()

        except Exception,e:
            db.session.rollback()
            return UTIL.to_json(status=1,message='failed',result=str(e))
        finally:
            db.session.close()
        return UTIL.to_json(status=0,message="update data success")

    def post(self):
        args = self.reqparse.parse_args()

        try:
            db.session.begin()

            userinfo= UserInfo(user_name=args['user_name'],
                        user_sex=args['user_sex'],
                        user_age=args['user_age'],
                        user_phone=args['user_phone'],
                        user_addr=args['user_addr'])

            db.session.add(userinfo)
            db.session.flush()
            db.session.commit()

        except Exception,e:
            db.session.rollback()
            return UTIL.to_json(status=1,message='add userinfo failed, error message :%s' %(str(e)))
        finally:
            db.session.close()
        return UTIL.to_json(status=0,message="add data success")

    def delete(self):
        user_id = request.args.get('user_id',None,type=int)
        try:
            db.session.begin()
            ad =UserInfo.query.get(user_id)
            if not ad:
                return UTIL.to_json(status=1,message='userinfo id %s not exist' % user_id)
            db.session.delete(ad)
            db.session.commit()
            return UTIL.to_json(status=0,message='delete userinfo success')
        except Exception,e:
            db.session.rollback()
            return UTIL.to_json(status=1,message='failed',result=str(e))
        finally:
            db.session.close()





