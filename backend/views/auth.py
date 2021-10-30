from . import auth
from flask import jsonify, request
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jti, get_raw_jwt
)

from module import db, auth_jti
import bcrypt
import time

@auth.route('/login', methods=['POST'])
def login():
    user_id = request.json.get("userId", None)
    password = request.json.get("password", None)

    if not user_id or password:
        return jsonify({"message": "foo"})
