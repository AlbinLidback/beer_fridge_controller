#!/usr/bin/env python3

from bottle import Bottle, response, request, template

app = Bottle()

page_text = {'title': 'PLZ WORK!',
            }

@app.route('/', method = "GET")
def index():
    """Home page"""

    #return template('simple.tpl', page_text)
    return template('simple.tpl', page_text, message="Please enter your name")

@app.route('/', method = "POST")
def formhandler():
    """Handle the form submission"""

    first = request.forms.get('first', type = str)
    last = request.forms.get('last', type = str)
    
    message = "Hello " + first + " " + last + "."
    
    return template("simple.tpl",page_text, message=message) 

#@app.route('/person/<who:path>')
#def homepage(who):
#    """Generate the home page for a person"""
#
#    return "<p>This is the home page for " + who + ".</p>"

#def dict_to_html(dd):
#    """Generate an HTML list of the keys and
#    values in the dictionary dd, return a
#    string containing HTML"""
#
#    print(dd)
#
#    html = "<ul>"
#    for key in dd.keys():
#        html += "<li><strong>%s: </strong>%s</li>" % (key, dd[key])
#    html += "</ul>"
#    return html

#@app.route('/about')
#def about():
#    response.content_type = 'text/plain'
#    return "Tell me about yourself."

#@app.route('/about')
#def about():
#
#    result = dict_to_html(request.environ)
#
#    return result
    
if __name__ == '__main__':
    app.run(debug=True, reloader=True)