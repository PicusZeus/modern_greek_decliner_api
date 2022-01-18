from files.db import db
from sqlalchemy.exc import IntegrityError


def save_to_db(self):
    db.session.add(self)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


def find_id_by_name(cls, name):

    model = db.session.query(cls).filter_by(name=name)
    if model:
        return model.id
    else:
        return None


class Poses(db.Model):
    # stores basic POSes used in lemmata
    __tablename__ = 'poses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))
    lemmata = db.relationship('GreekLemmata', lazy='dynamic')

    def __init__(self, pos, full__name):
        self.name = pos
        self.full_name = full__name

    @classmethod
    def find_id_by_name(cls, pos_name):
        return find_id_by_name(cls, pos_name)

    def save_to_db(self):
        save_to_db(self)


class Cases(db.Model):
    __tablename__ = 'cases'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, case, full_name):
        self.name = case
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, case_name):
        return find_id_by_name(cls, case_name)

    def save_to_db(self):
        save_to_db(self)


class Persons(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33), unique=True)

    def __init__(self, person, full_name):
        self.name = person
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, person_name):
        return find_id_by_name(cls, person_name)

    def save_to_db(self):
        save_to_db(self)


class Numbers(db.Model):
    __tablename__ = 'numbers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33), unique=True)

    def __init__(self, number, full_name):

        self.name = number
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, number_name):
        return find_id_by_name(cls, number_name)

    def save_to_db(self):
        save_to_db(self)


class Genders(db.Model):
    __tablename__ = 'genders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, gender, full_name):
        self.name = gender
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, gender_name):
        return find_id_by_name(cls, gender_name)

    def save_to_db(self):
        save_to_db(self)


class Aspects(db.Model):
    __tablename__ = 'aspects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33), unique=True)

    def __init__(self, aspect, full_name):
        self.name = aspect
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, aspect_name):
        return find_id_by_name(cls, aspect_name)

    def save_to_db(self):
        save_to_db(self)


class Voices(db.Model):
    __tablename__ = 'voices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33), unique=True)

    def __init__(self, voice, full_name):
        self.name = voice
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, voice_name):
        return find_id_by_name(cls, voice_name)

    def save_to_db(self):
        save_to_db(self)


class SecondaryPoses(db.Model):
    # stores secondary POSes like infinitive, superlative etc used in models
    __tablename__ = 'secondary_poses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, pos, full__name):
        self.name = pos
        self.full_name = full__name

    @classmethod
    def find_id_by_name(cls, pos_name):
        return find_id_by_name(cls, pos_name)

    def save_to_db(self):
        save_to_db(self)


class Tenses(db.Model):

    # stores tenses, but only three,that is final and past and future,
    # though in Greek and Polish the last one wont be used

    __tablename__ = 'tenses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, tense, full__name):
        self.name = tense
        self.full_name = full__name

    @classmethod
    def find_id_by_name(cls, tense_name):
        return find_id_by_name(cls, tense_name)

    def save_to_db(self):
        save_to_db(self)


class Moods(db.Model):

    # stores tenses, but only three,that is final and past and future,
    # though in Greek and Polish the last one wont be used

    __tablename__ = 'moods'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, mood, full__name):
        self.name = mood
        self.full_name = full__name

    @classmethod
    def find_id_by_name(cls, mood_name):
        return find_id_by_name(cls, mood_name)

    def save_to_db(self):
        save_to_db(self)



class GreekTenses(db.Model):

    __tablename__ = 'greek_tenses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(33), unique=True)
    tense_id = db.Column(db.Integer, db.ForeignKey('tenses.id'), nullable=False)
    tense = db.relationship('Tenses')
    mood_id = db.Column(db.Integer, db.ForeignKey('moods.id'), nullable=False)
    mood = db.relationship('Moods')
    aspect_id = db.Column(db.Integer, db.ForeignKey('aspects.id'), nullable=False)
    aspect = db.relationship('Aspects')
    particle_id = db.Column(db.Integer, db.ForeignKey('greek_forms.id'), nullable=False)
    particle = db.relationship('GreekForms')

    def __init__(self, greek_tense_name, tense_id, mood_id, aspect_id, particle_id):
        self.name = greek_tense_name
        self.tense_id = tense_id
        self.mood_id = mood_id
        self.aspect_id = aspect_id
        self.particle_id = particle_id

    def save_to_db(self):
        save_to_db(self)