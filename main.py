from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi, this basic app was created by Nikolay Denisov.'

@app.route('/secure')
def secure():
    return 'Some secret staff here'
