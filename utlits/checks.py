from __future__ import annotations
from flask import session, redirect, current_app as app, abort, request, jsonify
from functools import wraps
from .objects import convert_data_user
from datetime import datetime
from flask_jwt_extended import decode_token

def is_auth(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        authorization = request.headers.get('Authorization')
        if not authorization:
            return jsonify({"error": "No authorization"}), 400
        type_token, token = authorization.split(' ')[0], authorization.split(' ')[1]
        if type_token != "Bearer":
            return jsonify({"error": "Inviled token type"}), 400
        user_id = decode_token(token).get("sub").get("user_id")
        user_data = app.logins.find_one({"_id": user_id})
        if token:
            user = convert_data_user(user_data)
            if datetime.now() >= user.expires_in:
                token = app.auth.refresh_token(user.access_token)
                user = app.auth.user(token)
                data = app.logins.find_one({"_id": user.id})
                if not data:
                    app.logins.insert_one(user.as_dict)
                else :
                    app.logins.update_one({"_id": user.id}, {"$set": user.as_dict})
            
            # Success!
            return function_to_protect(*args, **kwargs)
        return redirect(f"/login?next={request.path}" )
    return wrapper

def check_permission(function_to_protect):
    @wraps(function_to_protect)
    def deco(*args, **kwargs):
        user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
        if is_admin(user.id):
            return function_to_protect(*args, **kwargs)
        guild = app.auth.get_guild(user.access_token, kwargs.get("guild_id"))
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
        user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
        if not is_admin(user.id):
            return abort(403)
        return function_to_protect(*args, **kwargs)
    return deco

