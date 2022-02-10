from __future__ import annotations
from flask import session, redirect, current_app
from functools import wraps
import typing as t
import requests

from utlits.objects import Channel, GuildInfo, Role


def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        if "token" in session:
            # Success!
            return function_to_protect(*args, **kwargs)
        return redirect("/login")
    return wrapper


def check_guild(guild_id: int) -> bool:
    r = requests.get(f"{current_app.config['BOT_SERVER']}/get_guild/{guild_id}")
    return r.json().get("status")

def guild_info(guild_id: int) -> GuildInfo:
    r = requests.get(f"{current_app.config['BOT_SERVER']}/get_guild/{guild_id}/info")
    return GuildInfo(**r.json().get("guild"))

def get_guild_channels(guild_id: int) -> t.Optional[t.List[Channel]]:
    r = requests.get(f"{current_app.config['BOT_SERVER']}/get_guild/{guild_id}/channels")
    return [Channel(**i) for i in r.json().get("channels")]

def get_shards_count():
    r = requests.get(f"{current_app.config['BOT_SERVER']}/shards_count")
    return r.json().get("count")

def get_guilds_count():
    r = requests.get(f"{current_app.config['BOT_SERVER']}/guilds_count")
    return r.json().get("count")

def get_users_count():
    r = requests.get(f"{current_app.config['BOT_SERVER']}/users_count")
    return r.json().get("count")

def get_channels_count():
    r = requests.get(f"{current_app.config['BOT_SERVER']}/channels_count")
    return r.json().get("count")

def get_guild_roles(guild_id: int):
    r = requests.get(f"{current_app.config['BOT_SERVER']}/get_guild/{guild_id}/roles")
    return [Role(**i) for i in r.json().get("roles")]
