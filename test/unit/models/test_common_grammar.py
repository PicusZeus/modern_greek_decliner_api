from test.unit.unit_base_test import UnitBaseTest
from models.common_grammar import Poses, Persons, SecondaryPoses, Cases, Voices, Tenses, Aspects, Numbers, Genders, Moods, GreekTenses


class CommonGrammar(UnitBaseTest):

    def test_poses(self):
        pos = Poses('verb', 'verb')
        self.assertEqual(pos.full_name, 'verb')
        self.assertEqual(pos.name, 'verb')

    def test_persons(self):
        person = Persons('pr', 'first')
        self.assertEqual(person.name, 'pr')
        self.assertEqual(person.full_name, 'first')

    def test_secondary_poses(self):
        sec_pos = SecondaryPoses('comp', 'comparative')
        self.assertEqual(sec_pos.name, 'comp')
        self.assertEqual(sec_pos.full_name, 'comparative')

    def test_cases(self):
        case = Cases('nom', 'nominative')
        self.assertEqual(case.name, 'nom')
        self.assertEqual(case.full_name, 'nominative')

    def test_voices(self):
        voice = Voices('pass', 'passive')
        self.assertEqual(voice.name, 'pass')
        self.assertEqual(voice.full_name, 'passive')

    def test_tenses(self):
        tense = Tenses('pres', 'present')
        self.assertEqual(tense.name, 'pres')
        self.assertEqual(tense.full_name, 'present')

    def test_aspects(self):
        aspect = Aspects('perf', 'perfect')
        self.assertEqual(aspect.name, 'perf')
        self.assertEqual(aspect.full_name, 'perfect')

    def test_numbers(self):
        number = Numbers('pl', 'plural')
        self.assertEqual(number.name, 'pl')
        self.assertEqual(number.full_name, 'plural')

    def test_genders(self):
        gender = Genders('fem', 'feminine')
        self.assertEqual(gender.name, 'fem')
        self.assertEqual(gender.full_name, 'feminine')

    def test_moods(self):
        mood = Moods('ind', 'indicative')
        self.assertEqual(mood.name, 'ind')
        self.assertEqual(mood.full_name, 'indicative')

    def test_greek_tenses(self):
        greek_tense = GreekTenses('present', 1, 1, 1, 1)
        self.assertEqual(greek_tense.name, 'present')
        self.assertEqual(greek_tense.tense_id, 1)