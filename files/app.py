import os

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_jwt import JWTError
from flask_restful import Api

from resources.modern_grammar import Lemmata
from resources.user import User, UserRegister, UserLogout, UserLogin, TokenRefresh
from .blacklist import BLACKLIST

app = Flask(__name__)
# app.config.from_object('files.config.DevelopmentConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

api = Api(app)


# create tables
@app.before_first_request
def create_tables():
    from files.db import db
    db.create_all()


jwt = JWTManager(app)


@app.errorhandler(JWTError)
def auth_error_handler(err):
    return jsonify({'message': 'Could not authorize'}), 401


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify(
        {
            'message': 'The token has expired',
            'error': 'token_expired'
        }
    ), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'description': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return ({
        'description': 'The token is not fresh',
        'error': 'fresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        "description": "The token has been revoked",
        "error": "token_revoked"
    })


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(Lemmata, '/lemma/<lemma>')


def create_app():
    db.init_app(app)
    return app


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
