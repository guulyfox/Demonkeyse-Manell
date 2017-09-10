# -*- coding: utf-8 -*-
__author__ = 'wenyao'
from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import create_engine


class APP(Flask):
    def __init__(self,config):
        Flask.__init__(self,__name__)
        self.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' %(config.mysql["user"],
                                                                            config.mysql["password"],
                                                                            config.mysql["host"], config.mysql["port"],
                                                                            config.mysql["database"])
        self.config['SQLALCHEMY_ECHO'] = False
        self.config['SQLALCHEMY_POOL_SIZE'] = int(config.mysql["db-connection-pool"])
        self.config['DEBUG'] = False
        self.db = SQLAlchemy(self,session_options={'autocommit': True})
    def get_db(self):
        return self.db

    def get_scoped_session(self):
        return self.db.create_scoped_session()

    def get_api(self):
        return Api(self,catch_all_404s=True)

    def get_excel(self):
        return excel


