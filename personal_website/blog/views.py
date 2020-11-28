"""
Contains all the routes (views) needed for the main blueprint.
Things such as functions and forms should be in separate files.
"""

from flask import render_template
from sqlalchemy import desc

from personal_website.models import Blogs
from . import blog


@blog.route('/')
def blog_homepage():
    # pylint: disable=singleton-comparison
    """
    Displays the blogs homepage.
    :return:
    """
    blogs = Blogs.query.filter(Blogs.hidden == False).order_by(desc(Blogs.start_date)).all()
    return render_template('blog.html', blogs=blogs, last_updated='2020-10-17')


@blog.route('/<link>')
def blog_post(link):
    """
    Displays specific blog via templating.
    :param link:
    :return:
    """
    post = Blogs.query.filter_by(link=link).first_or_404()
    return render_template('post.html', blog=post, last_updated=post.last_updated, onload='slideShow()')
