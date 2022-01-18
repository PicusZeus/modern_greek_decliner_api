from test.unit.unit_base_test import UnitBaseTest
from models.modern_greek import GreekLemmata, GreekForms


class ModernGreek(UnitBaseTest):

    def test_greek_lemmata(self):
        greek_lemma = GreekLemmata('άνθρωπος', 3, 'comment')
        self.assertEqual(greek_lemma.name, 'άνθρωπος')
        self.assertEqual(greek_lemma.pos_id, 3)
        self.assertEqual(greek_lemma.comments, 'comment')

    def test_greek_forms(self):
        greek_form = GreekForms('κάνει', 'κανει', 'kanei', person_id=3, number_id=1, gender_id=0, aspect_id=3,
                                case_id=0, lemma_id=232, voice_id=1, object_case_id=2, secondary_pos_id=3, tense_id=1)
        self.assertEqual(greek_form.form, 'κάνει')
        self.assertEqual(greek_form.unaccented_form, 'κανει')
        self.assertEqual(greek_form.latin_transcription, 'kanei')
        self.assertEqual(greek_form.person_id, 3)
        self.assertEqual(greek_form.number_id, 1)
        self.assertEqual(greek_form.gender_id, 0)
        self.assertEqual(greek_form.aspect_id, 3)
        self.assertEqual(greek_form.case_id, 0)
        self.assertEqual(greek_form.lemma_id, 232)
        self.assertEqual(greek_form.voice_id, 1)
        self.assertEqual(greek_form.object_case_id, 2)
        self.assertEqual(greek_form.secondary_pos_id, 3)
        self.assertEqual(greek_form.tense_id, 1)
