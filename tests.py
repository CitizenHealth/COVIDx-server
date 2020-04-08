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
            SQLALCHEMY_DATABASE_URI='mysql://admin@localhost/covidx_test'
        )

        return app

    def setUp(self):
        """
        called at the start of every test
        """

        db.create_all()

        test_user = User(user_id="1", display_name="john doe", email="jd21@gmail.com")
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
    def test_auth_login(self):
        response = self.client.get(url_for("auth.login_user"))
        self.assertEqual(response.status_code, 200)

    def test_auth_create(self):
        response = self.client.post(url_for("auth.create_user"), 
                                    data=dict(
                                        user_id="2", 
                                        display_name="jane doe", 
                                        email="janed@gmail.com")
                                    )
        self.assertEqual(response.status_code, 200)

    def test_auth_update(self):
        response = self.client.put(url_for("auth.update_user"), 
                                    data = dict(user_id="1", sex="female"))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()