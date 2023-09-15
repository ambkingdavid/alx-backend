#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    babel configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.debug = True
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    get the best matching language
    """
    user_languages = request.accept_languages
    # Choose the best match from the supported languages
    return user_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    index page
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
