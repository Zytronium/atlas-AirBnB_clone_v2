#!/usr/bin/python3
"""
flask thing for web server
"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State

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


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def n_odd_or_even(n):
    if n.isdigit():
        parity = "even" if int(n) % 2 == 0 else "odd"
        return render_template("6-number_odd_or_even.html",
                               number=n, parity=parity)
    else:
        abort(404)

@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template("7-states_list.html",
                           states=sorted(storage.all(State).values(),
                                         key=lambda x: x.name))

@app.teardown_appcontext
def teardown(exception):
    storage.close()



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
