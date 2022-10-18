from flask import Flask

app = Flask(__name__)

# Routing
@app.route('/')
def index():
    return '<h1>Hello Flask world!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, dear {}!</h1>'.format(name)

#flask --app hello run