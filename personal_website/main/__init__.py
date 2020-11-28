"""
Initialises the main blueprint used while building app.
"""
from flask import Blueprint

main = Blueprint('main', __name__)

# imports have to remain down here to prevent circular import errors
from . import views  # pylint: disable=wrong-import-position
