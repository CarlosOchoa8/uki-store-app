import functools
import json
from typing import Any

from flask import g, jsonify, redirect, url_for
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import NotFound
from auth.jwt_settings import bcrypt
from models import User


def get_current_user(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not g.user:
            return redirect(url_for("auth.sign_in"))
        return view(**kwargs)
    return wrapped_view

def generate_token(user_data: Any):
    """Generate token with jwt extended if user authenticate correctly."""
    if user := User.query.filter_by(email=user_data["email"]).first():
        hs_password = user.password
        password = user_data["password"]

        if bcrypt.check_password_hash(hs_password, password):
            user_json = user.to_json()
            access_token = create_access_token(identity=user_json)
            token_json = jsonify(access_token=access_token)
            return token_json, user

    message = "Los datos son incorrectos."
    raise NotFound(message)
