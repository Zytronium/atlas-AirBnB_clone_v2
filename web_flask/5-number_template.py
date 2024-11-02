#!/usr/bin/python3
"""
flask thing for web server
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def n_is_numb(n):
    if n.isdigit():
        return f"{n} is a number"
    else:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def n_template_is_numb(n):
    if n.isdigit():
        return render_template("5-number.html", number=n)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
