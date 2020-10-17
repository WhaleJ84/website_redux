
from flask import render_template, redirect, url_for, flash

from . import main
from personal_website.models import Blogs
from .forms import ContactForm


@main.route('/')
@main.route('/index')
@main.route('/home')
def index():
    recent = Blogs.query.filter(Blogs.hidden == False).order_by(Blogs.created.desc()).limit(5)
    latest = Blogs.query.filter(Blogs.hidden == False).order_by(Blogs.created.desc()).first()
    return render_template('index.html', recent=recent, latest=latest, last_updated='2019-07-08')


@main.route('/about')
def about():
    return render_template('about.html', last_updated='2019-04-19')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash('Name: {}, Email: {}, Message: {} | SENT'.format(name, email, message))
        return redirect(url_for('index'))
    flash('WARNING: This contact form does not work. Any information input will be lost.')
    return render_template('contact.html', form=form, last_updated='2019-07-04')


@main.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html', last_updated='2019-04-22')


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html', last_updated='2020-10-17'), 404
