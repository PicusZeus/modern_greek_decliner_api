from test.integration.base_integration import BaseIntegrationTest
from models.modern_greek import GreekLemmata, GreekForms


class GreekLemma(BaseIntegrationTest):

    def test_insert(self):
        with self.app_context:
            lemma = GreekLemmata('lemma', 1, 'comment')
            lemma.save_to_db()
            id = lemma.find_id_by_name('lemma', 1)

            self.assertEqual(id, 1)

    def test_duplicates(self):
        with self.app_context:
            lemma = GreekLemmata('lemma', 1, 'comment')
            lemma2 = GreekLemmata('lemma', 1, 'sth')
            lemma.save_to_db()
            lemma2.save_to_db()
            _all = GreekLemmata.query.all()
            self.assertEqual(len(_all), 1)

            lemma3 = GreekLemmata('lemma2', 1, 'sth')
            lemma3.save_to_db()
            _all = GreekLemmata.query.all()
            self.assertEqual(len(_all), 2)

            lemma4 = GreekLemmata('lemma2', 2, 'sth')
            lemma4.save_to_db()
            _all = GreekLemmata.query.all()
            self.assertEqual(len(_all), 3)