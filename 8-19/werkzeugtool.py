#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    response = Response("Hello %s!" % request.args.get("name", "World!"))
    return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple("192.168.0.73", 4000, application)
