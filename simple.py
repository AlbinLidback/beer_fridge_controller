#!/usr/bin/env python

from bottle import route, run

@route('/message')
def hello():
    return "Today is a beautiful day"  

run(host='localhost', port=8080, debug=True)