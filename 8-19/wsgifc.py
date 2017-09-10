#!/usr/bin/env python3
from wsgiref.simple_server import make_server
POST = 12018
HOST = "192.168.0.73"


def application(environ, start_response):
    start_response("200 OK",[('Content-Type','text/html')])
    return '<h1>Hello, web</h1>'

if __name__ == "__main__":
    httpd = make_server(HOST, POST, application)
    httpd.serve_forever()
