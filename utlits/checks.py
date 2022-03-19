from __future__ import annotations
from flask import session, redirect, current_app, abort, request, jsonify
from functools import wraps
from .auth import Auth
from .local_api import get_guild_channels

auth = Auth(current_app.config['CLIENT_ID'], current_app.config['CLIENT_SECRET'], current_app.config['REDIRECT_URI'])

def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        if "token" in session:
            # Success!
            return function_to_protect(*args, **kwargs)
        return redirect("/login")
    return wrapper

def check_permission(function_to_protect):
    @wraps(function_to_protect)
    def deco(*args, **kwargs):
        guild = auth.user(session['token']).get_guild(kwargs.get("guild_id"))
        if not guild:
            return abort(403)
            # Success!
        return function_to_protect(*args, **kwargs)
    return deco
