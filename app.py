#greet
from flask import Flask

app = Flask(__name__)

@app.routes('/welcome')
def welcome():
    return "welcome"

@app.routes('/welcome/home')
def welcome_home():
    return "welcome home"

@app.routes('/welcome/back')
def welcome_back():
    return "welcome back"
