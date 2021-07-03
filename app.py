from flask import flask

@app.routes('/welcome')
def welcome():
    return "welcome"

@app.routes('/welcome/home')
def welcome_home():
    return "welcome home"

@app.routes('/welcome/back')
def welcome_back():
    return "welcome back"
