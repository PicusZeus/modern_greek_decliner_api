from files.db import db
from sqlalchemy.exc import IntegrityError


def save_to_db(self):
    db.session.add(self)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


def find_id_by_name(cls, column_name, name):
    model_str = f"db.session.query(cls).filter_by({column_name}='{name}')"
    model = eval(model_str).first()
    if model:
        return model.id
    else:
        return None


class Poses(db.Model):
    # stores basic POSes used in lemmata
    __tablename__ = 'poses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pos = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))
    lemmata = db.relationship('GreekLemmata', lazy='dynamic')

    def __init__(self, pos, full__name):
        self.pos = pos
        self.full_name = full__name

    @classmethod
    def find_id_by_name(cls, pos_name):
        return find_id_by_name(cls, "pos", pos_name)

    def save_to_db(self):
        save_to_db(self)


class Cases(db.Model):
    __tablename__ = 'cases'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    case = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, case, full_name):
        self.case = case
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, case_name):
        return find_id_by_name(cls, 'case', case_name)

    def save_to_db(self):
        save_to_db(self)


class Persons(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33), unique=True)

    def __init__(self, person, full_name):
        self.person = person
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, person_name):
        return find_id_by_name(cls, 'person', person_name)

    def save_to_db(self):
        save_to_db(self)


class Numbers(db.Model):
    __tablename__ = 'numbers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33), unique=True)

    def __init__(self, number, full_name):

        self.number = number
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, number_name):
        return find_id_by_name(cls, 'number', number_name)

    def save_to_db(self):
        save_to_db(self)


class Genders(db.Model):
    __tablename__ = 'genders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, gender, full_name):
        self.gender = gender
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, gender_name):
        return find_id_by_name(cls, 'gender', gender_name)

    def save_to_db(self):
        save_to_db(self)


class Aspects(db.Model):
    __tablename__ = 'aspects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aspect = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33), unique=True)

    def __init__(self, aspect, full_name):
        self.aspect = aspect
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, aspect_name):
        return find_id_by_name(cls, 'aspect', aspect_name)

    def save_to_db(self):
        save_to_db(self)


class Voices(db.Model):
    __tablename__ = 'voices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voice = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33), unique=True)

    def __init__(self, voice, full_name):
        self.voice = voice
        self.full_name = full_name

    @classmethod
    def find_id_by_name(cls, voice_name):
        return find_id_by_name(cls, 'voice', voice_name)

    def save_to_db(self):
        save_to_db(self)


class SecondaryPoses(db.Model):
    # stores secondary POSes like infinitive, superlative etc used in models
    __tablename__ = 'secondary_poses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    secondary_pos = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, pos, full__name):
        self.secondary_pos = pos
        self.full_name = full__name

    @classmethod
    def find_id_by_name(cls, pos_name):
        return find_id_by_name(cls, "secondary_pos", pos_name)

    def save_to_db(self):
        save_to_db(self)


class Tenses(db.Model):

    # stores tenses, but only three,that is final and past and future,
    # though in Greek and Polish the last one wont be used

    __tablename__ = 'tenses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tense = db.Column(db.String(33), unique=True)
    full_name = db.Column(db.String(33))

    def __init__(self, tense, full__name):
        self.tense = tense
        self.full_name = full__name

    @classmethod
    def find_id_by_name(cls, tense_name):
        return find_id_by_name(cls, "tense", tense_name)

    def save_to_db(self):
        save_to_db(self)

