from unittest import TestCase
from files.app import app
from files.db import db


class BaseIntegrationTest(TestCase):

    SQLALCHEMY_DB_URI = "sqlite://"

    @classmethod
    def setUpClass(cls):
        app.config['DEBUG'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = cls.SQLALCHEMY_DB_URI
        with app.app_context():
            db.init_app(app)

    def setUp(self):
        with app.app_context():
            db.create_all()
        self.app = app.test_client()
        self.app_context = app.app_context()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()