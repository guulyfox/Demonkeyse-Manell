#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("Hello World!")

@app.route('/username/<string:username>/age/<int:age>')
def hubiwu_name(username,age):
    return ("Hello NO {0} {1}".format(username,age))

if __name__ == '__main__':
    app.run()
