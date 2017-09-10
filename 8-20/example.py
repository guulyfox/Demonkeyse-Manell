#!/usr/bin/python3

from flask import Flask
from flask.ext import restful
import flask_restful
app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello':'world'}
    def post(self):
        return {'hello':'post'}


api.add_resource(HelloWorld,"/")


if __name__ == '__main__':
    app.run(host = "192.168.0.73", port=808, debug = True)
