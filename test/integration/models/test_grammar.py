from test.integration.base_integration import BaseIntegrationTest
from resource_data import resources_grammar
from models.common_grammar import Cases, Tenses, Voices, Poses, SecondaryPoses, Persons, Numbers, Genders, Aspects, Moods, GreekTenses


class GrammarTerms(BaseIntegrationTest):

    def common_test(self, gram_term_table, term_class):
        for term, term_full in gram_term_table.items():
            t = term_class(term, term_full)
            t.save_to_db()

        terms_model = term_class.query.all()
        terms_in_db = [t.name for t in terms_model]
        terms = [t for t in gram_term_table.keys()]
        self.assertListEqual(terms_in_db, terms)

        for term, term_full in gram_term_table.items():
            t = term_class(term, term_full)
            t.save_to_db()

        terms_in_db = [t.name for t in terms_model]
        self.assertListEqual(terms_in_db, terms)

    def test_cases(self):
        with self.app_context:
            self.common_test(resources_grammar.cases, Cases)

    def test_tenses(self):
        with self.app_context:
            self.common_test(resources_grammar.common_tenses, Tenses)

    def test_voices(self):
        with self.app_context:
            self.common_test(resources_grammar.voices, Voices)

    def test_poses(self):
        with self.app_context:
            self.common_test(resources_grammar.poses, Poses)

    def test_secondary_poses(self):
        with self.app_context:
            self.common_test(resources_grammar.secondary_poses, SecondaryPoses)

    def test_persons(self):
        with self.app_context:
            self.common_test(resources_grammar.persons, Persons)

    def test_numbers(self):
        with self.app_context:
            self.common_test(resources_grammar.numbers, Numbers)

    def test_genders(self):
        with self.app_context:
            self.common_test(resources_grammar.genders, Genders)

    def test_aspects(self):
        with self.app_context:
            self.common_test(resources_grammar.aspects, Aspects)

    def test_moods(self):
        with self.app_context:
            self.common_test(resources_grammar.moods, Moods)

    def test_greek_tenses(self):
        with self.app_context:
            gr_tense = GreekTenses('future', 1, 1, 1, 1)
            gr_tense.save_to_db()
            gr_tense2 = GreekTenses('future', 1, 1, 1, 1)
            gr_tense2.save_to_db()

            all_tenses = GreekTenses.query.all()

            self.assertEqual(len(all_tenses), 1)
