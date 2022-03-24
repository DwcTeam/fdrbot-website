from __future__ import annotations
from flask import session, redirect, current_app as app, abort, request
from functools import wraps
from .objects import convert_data_user
from datetime import datetime


def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        token = session.get("token", None)
        if token:
            user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
            
            # If access_token is expired
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
        guild = app.auth.get_guild(user.access_token ,kwargs.get("guild_id"))
        print(guild)
        if not guild:
            return abort(403)
            # Success!
        return function_to_protect(*args, **kwargs)
    return deco

def is_admin(user_id: int):
    return True if user_id in app.config["ADMINS"] else False
