from unittest import TestCase
from files.app import app
from files.app import app
from files.db import db
from test.system.base_test import BaseTest
import json


class TestLemma(BaseTest):
    def test_get_lemma_id(self):
        # db.init_app(app)

        with self.app() as c:
            resp = c.get('/lemma/a')
            self.assertEqual(resp.status_code, 404)
            self.assertEqual(json.loads(resp.get_data()), {
    "message": "Lemma Not Found"
})
