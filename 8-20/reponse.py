#!/usr/bin/python3

from flask import Flask, url_for
from flask import Response, make_response
from flask import request
app = Flask(__name__)
@app.route('/')
def v_index():
    rsp = make_response('go <a href = "%s">page2</a>' % url_for('v_page2'))
    rsp.set_cookie('user','JJJJohnny')
    return rsp
    # 

@app.route('/page2')
def v_page2():
    user = request.cookies['user']
    return ('you are %s' % user)

if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.0.73",port=12306)
