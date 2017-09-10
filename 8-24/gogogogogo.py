#!/usr/bin/python3
from flask import request
from flask import make_response
from flask import Flask
from flask import url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']= \
"mysql+pymysql://feng:@192.168.0.73/test"
db = SQLAlchemy(app)

@app.route('/')
def v_index():
    rep = make_response('go <a herf="%s">page2</a>'%url_for('v_page2'))
    rsp.set_cookie('user','JJJJjoasd')

@app.route('/page2')
def v_page2():
    user = request.cookies['user']
    return 'you are %s' % user



if __name__ == "__main__":
     class User(db.Model):
         __tablename__ = 'users'

         id = db.Column(db.Integer, primary_key=True)
         email = db.Column(db.String, unique = True)
         username = db.Column(db.String)
         passwd = db.Column(db.String)
         date = db.Column(db.String)
     aci = []
     aci = input("please input id email username passwd date in next raw.").split(" ")
     user = User(id = int(aci[0]), email= aci[1], username= aci[2], passwd = aci[3], date= aci[4])
     app.run(host="192.168.0.73", port=83, debug=True )
     db.session.add(user)
     db.session.commit()
