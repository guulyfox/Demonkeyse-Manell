#/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello,world'

@app.route('/userid/<int:user_id>/name/<string:name>/age/<int:age>')
def show_user(user_id,name,age):
    return "user id:{0} ,name is {1},age is {2}".format(user_id,name,age)

if __name__ == '__main__':
    app.run(host='192.168.0.73',port=12018)

