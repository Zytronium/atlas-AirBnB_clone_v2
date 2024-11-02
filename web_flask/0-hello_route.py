#!/bin/python3
import flask


app = flask.Flask(__name__)

@app.route('/', strict_slashes=False)

def index():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)