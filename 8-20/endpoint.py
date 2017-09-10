#!/usr/bin/python3
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/user/<username>', endpoint='weiyao')
def profile(username): pass

with app.test_request_context():
    print(url_for('weiyao', username='John Doe'))
