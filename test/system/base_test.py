from unittest import TestCase
from files.app import app
from files.db import db


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client
        self.context = app.app_context
        with app.app_context():
            db.init_app(app)
