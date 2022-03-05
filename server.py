#!/usr/bin/env python3

from bottle import get, post, request, run, HTTPResponse, abort
import credentials
import driver

@get('/')
def test():
    return "Test"

@get('/<element>/<comand>/<key>')
def post(element, comand, key):
    if (key  != credentials.key):
        return "Noppe"
    
    d = None

    if comand == 'on':
        d = driver.on(element)
    if comand == 'off':
        d = driver.off(element)
    if comand == 'toggle':
        d = driver.toggle(element)

    string = "Element: {}, Comand: {}, Driver {}".format(element, comand, d)
    return {string}

if __name__ == '__main__':
    run(host='localhost', port=credentials.PORT, debug=True, reloader=True)