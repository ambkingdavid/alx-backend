#!/usr/bin/env python3

"""Contains a flask app and a babel class"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Translates to the best match language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Index route for the flask app
    Returns:
            The translated text
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
