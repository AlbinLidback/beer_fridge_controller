#!/usr/bin/env python3

from bottle import Bottle, response, request, template

app = Bottle()

@app.route('/')
def index():
    """Home page"""

    info = {'title': 'Welcome Home!',
            'content': 'Hello World'
            }

    return template('simple.tpl', info)

@app.route('/person/<who:path>')
def homepage(who):
    """Generate the home page for a person"""

    return "<p>This is the home page for " + who + ".</p>"

def dict_to_html(dd):
    """Generate an HTML list of the keys and
    values in the dictionary dd, return a
    string containing HTML"""

    print(dd)

    html = "<ul>"
    for key in dd.keys():
        html += "<li><strong>%s: </strong>%s</li>" % (key, dd[key])
    html += "</ul>"
    return html

@app.route('/about')
def about():
    response.content_type = 'text/plain'
    return "Tell me about yourself."

#@app.route('/about')
#def about():
#
#    result = dict_to_html(request.environ)
#
#    return result
    
if __name__ == '__main__':
    app.run(debug=True, reloader=True)