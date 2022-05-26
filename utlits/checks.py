from __future__ import annotations
from flask import session, redirect, current_app as app, abort, request, jsonify
from functools import wraps

from utlits.rest import Auth
from .objects import convert_data_user
from datetime import datetime
from .encrypt import decrypt_token
from pymongo.collection import Collection

def is_auth(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        with app.app_context():
            col_logins: Collection = app.col_logins
            auth: Auth = app.auth
        authorization = request.headers.get('Authorization')
        if not authorization:
            return jsonify({"error": "No authorization"}), 400
        type_token, token = authorization.split(' ')[0], authorization.split(' ')[1]
        if type_token != "Bearer":
            return jsonify({"error": "Inviled token type"}), 400
        if token.split(".").__len__() != 2:
            return jsonify({"error": "Inviled token"}), 400
        try:
            user_id, access_token = decrypt_token(token)
        except:
            return jsonify({"error": "Inviled token"}), 400
        user_data = col_logins.find_one({"_id": user_id})
        user = convert_data_user(user_data)
        if not user.access_token.access_token.startswith(access_token):
            return jsonify({"error": "Inviled token"}), 400
        if token:
            if datetime.now() >= user.expires_in:
                token = auth.refresh_token(user.access_token)
                user = auth.user(token)
                data = col_logins.find_one({"_id": user.id})
                if not data:
                    col_logins.insert_one(user.as_dict)
                else :
                    col_logins.update_one({"_id": user.id}, {"$set": user.as_dict})
            
            # Success!
            return function_to_protect(*args, **kwargs)
        return redirect(f"/login?next={request.path}" )
    return wrapper

def check_permission(function_to_protect):
    @wraps(function_to_protect)
    def deco(*args, **kwargs):
        with app.app_context():
            col_logins: Collection = app.col_logins
            auth: Auth = app.auth
        user = convert_data_user(col_logins.find_one({"token.access_token": session["token"]}))
        if is_admin(user.id):
            return function_to_protect(*args, **kwargs)
        guild = auth.get_guild(user.access_token, kwargs.get("guild_id"))
        if not guild:
            return abort(403)
            # Success!
        return function_to_protect(*args, **kwargs)
    return deco

def is_admin(user_id: int):
    return True if user_id in app.config["ADMINS"] else False

def only_admin(function_to_protect):
    @wraps(function_to_protect)
    def deco(*args, **kwargs):
        with app.app_context():
            col_logins: Collection = app.col_logins
        user = convert_data_user(col_logins.find_one({"token.access_token": session["token"]}))
        if not is_admin(user.id):
            return abort(403)
        return function_to_protect(*args, **kwargs)
    return deco

