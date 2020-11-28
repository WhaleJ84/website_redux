"""
Contains all the forms needed for the main blueprint.
Things such as views and functions should be in separate files.
"""

from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class ContactForm(FlaskForm):
    """
    Specifies the fields WTForms will create in HTML.
    """
    name = StringField('Name:', validators=[validators.optional()])
    email = EmailField('Email:', validators=[validators.input_required(),
                                             validators.email('Not a valid email', False, True)])
    message = TextAreaField('Message:', validators=[validators.input_required()])
