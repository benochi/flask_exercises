from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

"""Basic math operations."""

@app.route('/add')
def add(a, b):
    """Add a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = add(a + b)

    return str(sum)

@app.route('/sub')
def sub(a, b):
    """Substract b from a."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = sub(a, b)

    return str(sum)

@app.route('/mult')
def mult(a, b):
    """Multiply a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = mult(a * b)

    return str(total)

@app.route('/div')
def div(a, b):
    """Divide a by b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = div(a / b)

    return str(total)

###Extra
operations = {
    "add": add,
    "sub": sub,
    "div": div,
    "mult": mult
}

@app.route("/math/<operation>")
def equations(operation):
    """perform operation on a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = operations[operation](a, b)

    return str(total)
