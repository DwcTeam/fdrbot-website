from __future__ import annotations
from flask import session, redirect, current_app as app, abort, request
from functools import wraps
from .auth import Auth
from .objects import AccessToken

auth = Auth(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'], app.config['REDIRECT_URI'])

def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        token = session.get("token", None)

        if token:
            user = app.logins.find_one({"token": token})
        if "token" in session:
            # Success!
            return function_to_protect(*args, **kwargs)
        return redirect(f"/login?next={request.path}" )
    return wrapper

def check_permission(function_to_protect):
    @wraps(function_to_protect)
    def deco(*args, **kwargs):
        user = auth.user(AccessToken(**app.logins.find_one({"token.access_token": session["token"]}).get("token")))
        guild = user.get_guild(int(request.args.get("guild_id")))
        if not guild:
            return abort(403)
            # Success!
        return function_to_protect(*args, **kwargs)
    return deco
