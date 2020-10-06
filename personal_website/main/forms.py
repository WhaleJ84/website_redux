
from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class ContactForm(FlaskForm):
    name = StringField('Name:', validators=[validators.optional()])
    email = EmailField('Email:', validators=[validators.input_required(),
                                             validators.email('Not a valid email', False, True)])
    message = TextAreaField('Message:', validators=[validators.input_required()])
