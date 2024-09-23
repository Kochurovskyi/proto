from flask import Flask

def say_hello(username="World"):
    return '<p>Hello %s!</p>\n' % username

header_text = '''<html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''<p><em>Hint</em>: This is a RESTful web service! Append a username
to the URL (for example: <code>/Thelonious</code>) to say hello to say hello to
someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'
app = Flask(__name__)

def index():
    return header_text + say_hello() + instructions + home_link + footer_text

def hello(username):
    return header_text + say_hello(username) + home_link + footer_text

app.add_url_rule('/', 'index', index)
app.add_url_rule('/<username>', 'hello', hello)

if __name__ == '__main__':
    app.run(debug=True)