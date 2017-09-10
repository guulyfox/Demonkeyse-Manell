#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/test')
def test():
    return 'this is response'
@app.route("/postUser", methods=["POST"])
def hello_user():
    return "Post User"

if __name__ == '__main__':
    app.run(host = "192.168.0.73", port =8181, debug = True)
