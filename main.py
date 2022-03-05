#!/usr/bin/env python3

from bottle import get, post, request, run, HTTPResponse, abort

PORT = 7007

@get('/')
def test():
    return {'Test'}

@get('/hej')
def test():
    return {'HEJ'}

run(host='localhost', port=PORT, debug=True, reloader=True)
