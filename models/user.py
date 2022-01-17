from files.db import db
from sqlalchemy.exc import IntegrityError


class UserModel(db.Model):
    query: db.Query
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    phoneNumber = db.Column(db.Integer)

#    posts = db.relationship("PostModel")

    def __init__(self, email, username, password, phone_number):

        self.email = email
        self.username = username
        self.password = password
        self.phoneNumber = phone_number

    @classmethod
    def find_by_username(cls, username):

        row = cls.query.filter_by(username=username).first()

        if row:
            user = row
        else:
            user = None

        return user

    @classmethod
    def find_by_id(cls, _id):
        row = cls.query.filter_by(id=_id).first()

        if row:
            user = row
        else:
            user = None

        return user

    @classmethod
    def find_by_email(cls, email):
        row = cls.query.filter_by(email=email).first()

        if row:
            user = row
        else:
            user = None
        return user

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {'message': 'username or email already registered'}

    def __str__(self):
        return str(self.id)
