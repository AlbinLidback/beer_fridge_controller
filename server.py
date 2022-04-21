#!/usr/bin/env python3

from bottle import Bottle, response, request, template

app = Bottle()

page_text = {'title': 'BFC',
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

    if request.forms.get('btn') == ON:
        driver.on("fridge")
    elif request.forms.get('btn') == OFF:
        driver.off("fridge")
    
if __name__ == '__main__':
    app.run(debug=True, reloader=True)