from werkzeug.security import safe_str_cmp
from flask_restplus import inputs, Resource, reqparse

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt
)

from models.user import UserModel
from files.blacklist import BLACKLIST

_user_parser = reqparse.RequestParser()

_user_parser.add_argument(
                        'password',
                        type=str,
                        required=True,
                        help='password required'
                        )
_user_parser.add_argument(
                        'email',
                        type=inputs.email(),
                        required=True,
                        help='email required'
                        )
_user_parser.add_argument(
                        'phoneNumber',
                        type=int,
                        required=False
                        )

class UserRegister(Resource):
    _user_parser.add_argument(
        'username',
        type=str,
        required=True,
        help='username required'
    )
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data["username"]) or UserModel.find_by_email(data['email']):
            return {"message": f"a user {data['username']} or {data['email']} already exists in db"}
        new_user = UserModel(None, **data)
        new_user.insert()

        return {"message": "user created successfully"}, 201


class User(Resource):

    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': "User Not Found"}, 404

        return user.json(), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': "User Not Found"}, 404
        user.delet()
        return {'message': "user deleted"}, 200

class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()

        user = UserModel.find_by_email(data['email'])
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {"mesage": 'Invalid credentials'}, 401

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return {'message': 'Successfully logged out'}, 200

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
