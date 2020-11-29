"""
Contains all the routes (views) needed for the main blueprint.
Things such as functions and forms should be in separate files.
"""

from flask import render_template, flash

from personal_website.models import Blogs
from . import main
from .forms import ContactForm


@main.route('/')
@main.route('/index')
@main.route('/home')
def index():
    # pylint: disable=singleton-comparison
    """
    Directs to the index (homepage).
    :return:
    """
    recent = Blogs.query.filter(Blogs.hidden == False).order_by(Blogs.created.desc()).limit(5)
    latest = Blogs.query.filter(Blogs.hidden == False).order_by(Blogs.created.desc()).first()
    return render_template('index.html', recent=recent, latest=latest, last_updated='2019-07-08')


@main.route('/about')
def about():
    """
    Directs to the about-me page.
    :return:
    """
    return render_template('about.html', last_updated='2019-04-19')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Directs to the contact page.
    :return:
    """
    form = ContactForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     email = form.email.data
    #     message = form.message.data
    #     flash('Name: {}, Email: {}, Message: {} | SENT'.format(name, email, message))
    #     return redirect(url_for('main.index'))
    flash('WARNING: This contact form does not work. Any information input will be lost.')
    return render_template('contact.html', form=form, last_updated='2019-07-04', onload='main()')


@main.route('/privacy_policy')
def privacy_policy():
    """
    Directs to the privacy policy page.
    :return:
    """
    return render_template('privacy_policy.html', last_updated='2019-04-22')


@main.app_errorhandler(404)
def page_not_found(error):
    """
    Redirects to the 404 error page.
    :param error:
    :return:
    """
    print(error)
    return render_template('404.html', last_updated='2020-10-17'), 404
