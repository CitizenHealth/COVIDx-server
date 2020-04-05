import unittest
import sys

from flask_testing import TestCase
from flask import abort, url_for

from app import create_app, db
from models.user import User

class TestBase(TestCase):

    def create_app(self):
        config_name="testing"
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql://admin:password@localhost/covidx_test'
        )

        return app

    def setUp(self):
        """
        called at the start of every test
        """

        db.create_all()

        test_user = User(id="1", name="test_user", email="test@gmail.com")
        db.session.add(test_user)
        # sys.stdout.write("Hello")
        db.session.commit()

    def tearDown(self):
        """
        called after every test
        """

        db.session.remove()
        db.drop_all()


class TestModels(TestBase):
    def test_user_model(self):
        self.assertEqual(User.query.count(), 1)


class TestViews(TestBase):
    def test_auth_view(self):
        response = self.client.get(url_for("auth.login_user"))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()