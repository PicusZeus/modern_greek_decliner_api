from unittest import TestCase
from files.app import app


class UnitBaseTest(TestCase):

    def setUp(self):
        self.client = app.test_client
