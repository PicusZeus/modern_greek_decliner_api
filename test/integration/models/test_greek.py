from test.integration.base_integration import BaseIntegrationTest
from models.modern_greek import GreekLemmata, GreekForms
from models.common_grammar import Poses

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


class GreekForm(BaseIntegrationTest):

    def test_insert(self):
        with self.app_context:
            greek_form = GreekForms('κάνω', 'κανω', 'kano', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
            greek_form.save_to_db()
            g_f = GreekForms.query.filter_by(form='κάνω').first()
            self.assertEqual(g_f.person_id, 1)

    def test_duplicates(self):
        with self.app_context:
            greek_form1 = GreekForms('κάνω', 'κανω', 'kano', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1).save_to_db()

            greek_form2 = GreekForms('κάνω', 'κανω', 'kano', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1).save_to_db()

            forms = GreekForms.query.filter_by(form='κάνω').all()
            self.assertEqual(len(forms), 1)

    def test_link_to_lemma(self):
        with self.app_context:
            lemma = GreekLemmata('κάνω', 1, 'comment')
            lemma.save_to_db()

            greek_form = GreekForms('κάνω', 'kano', 'kano', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
            greek_form.save_to_db()
            self.assertEqual(greek_form.lemma.name, 'κάνω')

    def test_link_to_pos(self):
        with self.app_context:
            pos = Poses