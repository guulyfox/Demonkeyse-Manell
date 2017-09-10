#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://feng:@192.168.0.73/student"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def v_index():
    return render_template("stuinfo.html")


class stuInfo(db.Model):
    __tablename__ = "stu"
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String)
    age = db.Column(db.Integer)
    num = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    grade = db.Column(db.Integer)
    sub = db.Column(db.String)
    name = db.Column(db.String, unique=True)

'''
class AdsList(Resource)
def get(self, maxline, pagenum):
    offset = (pagenum -1)*maxline
    limit = maxline
    ads_list = ADS.query.order_by(ADS.id.desc()).limit(limit).offset(offset)
    addslist =[]
    tmp_list =[]
    for i in ads_list
        adslist.append(i)
    for ads in adslist:
        tmp = {}
        tmp['']
'''

@app.route('/addinfo', methods=["POST"])
def addinfo():
    stu_info = stuInfo(\
    id= request.form['id'],\
    sex = request.form['sex'],\
    age = request.form['age'],\
    num = request.form['num'],\
    address = request.form['address'],\
    grade = request.form['grade'],\
    sub = request.form['sub'],\
    name = request.form['name']\
)
    db.session.add(stu_info)
    db.session.commit()
    return "submmit success!"

@app.route('/query', methods=["GET"])
def whatisthis():
    usersall = stuInfo.query.all()
    
    userselect = stuInfo.query.filter_by(username = '', email = '')
    userorder_by = stuInfo.query.oder_by(desc(stuInfo.name),stuInfo.address)
    usera = stuInfo.query.limit(10).offset(10)
    userslice = stuInfo.query.slicen(1,3)
    return userslice

if __name__=="__main__":
    app.run(host='192.168.0.73',port=8088,debug=True,threaded=True)
