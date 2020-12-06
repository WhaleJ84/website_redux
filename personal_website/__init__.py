"""
Imports the modules necessary to build the Flask application.
Module contains the `create_app` method to build the appropriate environment.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

from .config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    """
    Builds the Flask application based on the `config_name` passed.
    Available configs are: ['prod', 'test', 'dev'] and chooses 'dev' by default.

    :type config_name: str
    :rtype: object
    """
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    toolbar = DebugToolbarExtension(app)  # pylint: disable=unused-variable

    # blueprint imports have to remain down here to prevent circular import errors
    from .main import main as main_blueprint  # pylint: disable=import-outside-toplevel
    app.register_blueprint(main_blueprint)
    from .blog import blog as blog_blueprint  # pylint: disable=import-outside-toplevel
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    return app
