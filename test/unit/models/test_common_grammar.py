from test.unit.unit_base_test import UnitBaseTest
from models.common_grammar import Poses, Persons, SecondaryPoses, Cases, Voices, Tenses, Aspects, Numbers, Genders


class CommonGrammar(UnitBaseTest):

    def test_poses(self):
        pos = Poses('verb', 'verb')
        self.assertEqual(pos.full_name, 'verb')
        self.assertEqual(pos.pos, 'verb')

    def test_persons(self):
        person = Persons('pr', 'first')
        self.assertEqual(person.person, 'pr')
        self.assertEqual(person.full_name, 'first')

    def test_secondary_poses(self):
        sec_pos = SecondaryPoses('comp', 'comparative')
        self.assertEqual(sec_pos.secondary_pos, 'comp')
        self.assertEqual(sec_pos.full_name, 'comparative')

    def test_cases(self):
        case = Cases('nom', 'nominative')
        self.assertEqual(case.case, 'nom')
        self.assertEqual(case.full_name, 'nominative')

    def test_voices(self):
        voice = Voices('pass', 'passive')
        self.assertEqual(voice.voice, 'pass')
        self.assertEqual(voice.full_name, 'passive')

    def test_tenses(self):
        tense = Tenses('pres', 'present')
        self.assertEqual(tense.tense, 'pres')
        self.assertEqual(tense.full_name, 'present')

    def test_aspects(self):
        aspect = Aspects('perf', 'perfect')
        self.assertEqual(aspect.aspect, 'perf')
        self.assertEqual(aspect.full_name, 'perfect')

    def test_numbers(self):
        number = Numbers('pl', 'plural')
        self.assertEqual(number.number, 'pl')
        self.assertEqual(number.full_name, 'plural')

    def test_genders(self):
        gender = Genders('fem', 'feminine')
        self.assertEqual(gender.gender, 'fem')
        self.assertEqual(gender.full_name, 'feminine')