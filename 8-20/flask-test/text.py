#!/usr/bin/python3
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import CHAR, Integer, String
from flask import Flask

app=Flask(__name__)
Base =declarative_base()

class User(Base):
    __tablename__="user_info"
    id=Column(Integer,primary_key=True)
    user_name=Column(String(20))
    user_sex=Column(String(20))
    user_age=Column(Integer)
    user_phone=Column(String(20))
    user_addr=Column(String(20))

engine=create_engine('mysql+pymysql://wenyao:wenyao@192.168.0.201:3306/flasktest')
DBSession = sessionmaker(bind=engine)
session=DBSession()
new_user=User(user_name='guuly',user_sex='male',user_age='23',user_phone="AZ1010",user_addr="ACG")

session.add(new_user)
session.commit()
session.close()

