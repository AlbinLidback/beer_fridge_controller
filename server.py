#!/bin/bash

from bottle import Bottle, response, request, template
import RPi.GPIO as GPIO

app = Bottle()

page_text = {'title': 'Fridge Controller',
            'button_on': 'ON',
            'button_off': 'OFF'
            }

@app.route('/', method = "GET")
def index():
    """Home page"""

    return template('webpage.html', page_text, message = "")

@app.route('/', method = "POST")
def formhandler():
    """Handle the form submission"""
    
    message = "Received " + request.forms.get('btn')

    if request.forms.get('btn') =='ON':
        GPIO.output(2, GPIO.HIGH)
    elif request.forms.get('btn') == 'OFF':
        GPIO.output(2, GPIO.LOW)
    
    return template('webpage.html', page_text, message = "")
    
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2, GPIO.OUT)

    app.run(host='192.168.1.8', port='8080', debug=True, reloader=True)
