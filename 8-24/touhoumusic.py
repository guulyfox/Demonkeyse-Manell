#!/usr/bin/python3
from flask import request
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/reimu')
def temple():
    return 'Gen so kyo'

@app.route('/sakura', methods=['POST'])
def sakura():
    return 'uuz'

@app.route('/badapple', methods=['POST'])
def show_apple():
    return 'you name is {0} your passwd is {1}'.format(request.form['username'], request.form['password'])

@app.route('/')
def item():
    return '''<html>
    <body>
    <form method ="POST" action="/badapple">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="login">
    </form>
    </body>
    </html>
'''


@app.route('/login')
def demon():
    return render_template('login.html')

if __name__=='__main__':
    app.run(host='192.168.0.73', port=180, debug=True, threaded=True)
