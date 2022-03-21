import typing as t
import requests
from utlits.objects import Channel, GuildInfo, Role
from flask import current_app

def check_guild(guild_id: int) -> bool:
    r = requests.get(f"{current_app.config['BOT_SERVER']}/get_guild/{guild_id}")
    return r.json().get("status")

def guild_info(guild_id: int) -> GuildInfo:
    r = requests.get(f"{current_app.config['BOT_SERVER']}/get_guild/{guild_id}/info")
    return GuildInfo(**r.json().get("guild"))

def get_guild_channels(guild_id: int) -> t.Optional[t.List[Channel]]:
    r = requests.get(f"{current_app.config['BOT_SERVER']}/get_guild/{guild_id}/channels")
    return [Channel(**i) for i in r.json().get("channels")]

def get_guild_roles(guild_id: int):
    r = requests.get(f"{current_app.config['BOT_SERVER']}/get_guild/{guild_id}/roles")
    return [Role(**i) for i in r.json().get("roles")]

def get_commands() -> t.List[t.Dict]:
    r = requests.get(f"{current_app.config['BOT_SERVER']}/commands")
    return r.json().get("commands")

def get_bot_info() -> t.Dict:
    r = requests.get(f"{current_app.config['BOT_SERVER']}/bot_info")
    return r.json()

def send_ping():
    try:
        r = requests.get(f"{current_app.config['BOT_SERVER']}/ping")
        r.raise_for_status()
        return True
    except:
        return False
