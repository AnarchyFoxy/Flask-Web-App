from flask import Flask, abort, make_response, redirect, request

app = Flask(__name__)

# Routing
@app.route('/')
def index():
    return '<h1>Hello Flask world!</h1>'
    
# dynamic route
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, dear {}!</h1>'.format(name)

#returning agent info
@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<h1>You are using {} browser</h1>'.format(user_agent)

# setting HTTP status 400
@app.route('/status')
def status():
    return '<h1>This timeline is wrong</h1>', 400

# using reposne
@app.route('/response')
def response():
    response = make_response('<h1>This document contains cookie file!</h1>')
    response.set_cookie('response', '42')
    return response

# redirect example
@app.route('/redirect')
def redirect():
    return redirect('https://astryda-stories-7i7aspkfwq-lz.a.run.app')

# using abort function
@app.route('/abort/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)


#flask --app hello run