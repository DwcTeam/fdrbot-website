from __future__ import annotations
from flask import session, redirect, current_app
from functools import wraps
from typing import Any
from utlits import Guild

def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        if "token" in session:
            # Success!
            return function_to_protect(*args, **kwargs)
        return redirect("/login")
    return wrapper


def check_guild(guild_id: Any) -> dict | Any:
    token = session.get("token")
    guild = current_app.auth.user(token).get_guild(guild_id)
    if not guild:
        return {"Error": "Guild Not Found", "code": 0}
    if guild.get("code") == 1:
        return guild
    x = Guild(guild_id)
    if not x.info:
        x.insert()
    return x.info

