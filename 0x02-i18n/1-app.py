#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.debug = True
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """
    index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
