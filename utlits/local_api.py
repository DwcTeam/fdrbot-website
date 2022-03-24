import json
import typing as t
import requests
from utlits.objects import Channel, Guild, Role, convert_channels, convert_roles, BotGuild
from flask import current_app as app

def get_guild(guild_id: int) -> BotGuild:
    r = requests.get(f"{app.config['BOT_SERVER']}/guild/{guild_id}").json()
    return BotGuild(
        channels=convert_channels(r["channels"]),
        roles=convert_roles(r["roles"]),
    )

def get_commands() -> t.List[t.Dict]:
    r = requests.get(f"{app.config['BOT_SERVER']}/commands")
    return r.json().get("commands")

def get_bot_info() -> t.Dict:
    r = requests.get(f"{app.config['BOT_SERVER']}/info")
    return r.json()

def check_guild(guild_id: int) -> bool:
    r = requests.get(f"{app.config['BOT_SERVER']}/guild/{guild_id}/check")
    return r.json()["check"]

def check_guilds(guilds: t.List[Guild]) -> t.List[t.Dict]:
    r = requests.get(f"{app.config['BOT_SERVER']}/guilds/check", json={"guilds": [i.id for i in guilds]})
    return r.json()["guilds"]

def send_ping():
    try:
        r = requests.get(f"{app.config['BOT_SERVER']}/ping")
        r.raise_for_status()
        return True
    except:
        return False
