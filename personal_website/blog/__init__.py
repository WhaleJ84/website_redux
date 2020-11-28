"""
Initialises the blog blueprint used while building app.
"""
from flask import Blueprint

blog = Blueprint('blog', __name__)

# imports have to remain down here to prevent circular import errors
from . import views  # pylint: disable=wrong-import-position
