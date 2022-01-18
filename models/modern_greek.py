from files.db import db
from sqlalchemy.exc import IntegrityError
from models.common_grammar import Poses
from sqlalchemy import Column, Integer, String, ForeignKey
# from sq

def save_to_db(self):
    db.session.add(self)
    try:
        db.session.commit()
        # print('saved')
    except IntegrityError as e:
        # print(e)
        db.session.rollback()


class GreekLemmata(db.Model):
    __tablename__ = 'greek_lemmata'
    __table_args__ = (db.UniqueConstraint('name', 'pos_id'),)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    pos_id = db.Column(db.Integer, db.ForeignKey('poses.id'), nullable=False)
    pos = db.relationship('Poses')
    comments = db.Column(db.String(256))

    def __init__(self, name, pos_id, comments):
        self.name = name
        self.pos_id=pos_id
        self.comments = comments

    def save_to_db(self):
        save_to_db(self)

    @classmethod
    def find_id_by_name(cls, name, pos_id):
        lemma = cls.query.filter(cls.name == name, cls.pos_id == pos_id).first()
        if lemma:
            lemma_id = lemma.id

            return lemma_id
        else:
            return None

    def __str__(self):
        return f"id={self.id}, lemma={self.name}, pos={self.pos_id}"


class GreekForms(db.Model):
    query: db.Query
    __tablename__ = 'greek_forms'
    __table_args__ = (db.UniqueConstraint('form', 'person_id', 'number_id', 'gender_id', 'aspect_id',
                                          'lemma_id', 'case_id', 'voice_id', 'secondary_pos_id', 'tense_id'),)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    form = db.Column(db.Text(80), nullable=False)
    unaccented_form = db.Column(db.Text(80))  # easier searching
    latin_transcription = db.Column(db.Text(80))  # transcription to use with regexes
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    person = db.relationship('Persons')

    number_id = db.Column(db.Integer, db.ForeignKey('numbers.id'))
    number = db.relationship('Numbers')
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'))
    gender = db.relationship('Genders')
    aspect_id = db.Column(db.Integer, db.ForeignKey('aspects.id'))
    aspect = db.relationship('Aspects')
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'))
    case = db.relationship('Cases', foreign_keys='GreekForms.case_id')
    # in case a table has foreign keys pointing to the same table, to avoid ambiguity you have to add
    # foreign_keys="cls.sth_id"
    lemma_id = db.Column(db.Integer, db.ForeignKey('greek_lemmata.id'), nullable=False)
    lemma = db.relationship('GreekLemmata')
    voice_id = db.Column(db.Integer, db.ForeignKey('voices.id'))
    voice = db.relationship('Voices')
    object_case_id = db.Column(db.Integer, db.ForeignKey('cases.id'))
    object_case = db.relationship('Cases', foreign_keys='GreekForms.object_case_id')
    # less for verbs, more for preps
    secondary_pos_id = db.Column(db.Integer, db.ForeignKey('secondary_poses.id'))
    secondary_pos = db.relationship('SecondaryPoses')
    # these poses are more specific: adverb, comparative, participle etc
    tense_id = db.Column(db.Integer, db.ForeignKey('tenses.id'))
    tense = db.relationship('Tenses')



    def __init__(self, form, unaccented_form, latin_transcription, person_id, number_id, gender_id, aspect_id,
                 case_id, lemma_id, voice_id, object_case_id, secondary_pos_id, tense_id):
        self.form = form
        self.unaccented_form = unaccented_form
        self.latin_transcription = latin_transcription
        self.person_id = person_id
        self.number_id = number_id
        self.gender_id = gender_id
        self.aspect_id = aspect_id
        self.case_id = case_id
        self.lemma_id = lemma_id
        self.voice_id = voice_id
        self.object_case_id = object_case_id
        self.secondary_pos_id = secondary_pos_id
        self.tense_id = tense_id

    def save_to_db(self):

        save_to_db(self)


