#!/usr/bin/env python3

from bottle import get, post, request, run, HTTPResponse, abort
import credentials
import driver

@get('/')
def test():
    return "Test"

# http://localhost:7007/slinga_pin/toggle/aGfRSW5DLwZFiQ35hX0qGxWZwawYeFZ9
@get('/<element>/<comand>/<key>')
def post(element, comand, key):
    if (key  != credentials.key):
        return "Noppe"
    
    ret = None

    if comand == 'on':
        ret = driv.on(element)
    if comand == 'off':
        ret = driv.off(element)
    if comand == 'toggle':
        ret = driv.toggle(element)

    string = "Element: {}, Comand: {}, Driver {}".format(element, comand, ret)
    return string

if __name__ == '__main__':
    run(host='localhost', port=credentials.PORT, debug=True, reloader=True)
    driv = driver.driver()