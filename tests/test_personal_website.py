import unittest
from flask import url_for
from flask_testing import TestCase

import personal_website
# from personal_website.models import Blogs


class PersonalWebsiteTestCase(TestCase):
    def create_app(self):
        return personal_website.create_app('test')

    def setUp(self) -> None:
        self.db = personal_website.db
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        pass

    def test_index_response_code(self):
        response = self.client.get(url_for('main.index'), follow_redirects=True)
        PersonalWebsiteTestCase.assert200(self, response)

    def test_about_response_code(self):
        response = self.client.get(url_for('main.about'), follow_redirects=True)
        PersonalWebsiteTestCase.assert200(self, response)

    def test_contact_response_code(self):
        response = self.client.get(url_for('main.contact'), follow_redirects=True)
        PersonalWebsiteTestCase.assert200(self, response)

    def test_privacy_policy_response_code(self):
        response = self.client.get(url_for('main.privacy_policy'), follow_redirects=True)
        PersonalWebsiteTestCase.assert200(self, response)

    def test_blog_homepage_response_code(self):
        response = self.client.get(url_for('blog.blog_homepage'), follow_redirects=True)
        PersonalWebsiteTestCase.assert200(self, response)

    def test_blog_hackthesouth2019_response_code(self):
        response = self.client.get(url_for('blog.blog_post', link='hackthesouth2019'), follow_redirects=True)
        PersonalWebsiteTestCase.assert200(self, response)

    def test_blog_post_response_code(self):
        response = self.client.get(url_for('blog.blog_post', link='badlink'), follow_redirects=True)
        PersonalWebsiteTestCase.assert404(self, response)


if __name__ == '__main__':
    unittest.main()
