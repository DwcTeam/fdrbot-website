from __future__ import annotations
from requests import request
from dataclasses import dataclass
import typing as t


BASE = "https://discord.com/api/v9"
IMAGE_BASE = "https://cdn.discordapp.com"


class Permissions:
    CREATE_INSTANT_INVITE =        1 << 0
    KICK_MEMBERS =                 1 << 1
    BAN_MEMBERS =                  1 << 2
    ADMINISTRATOR =                1 << 3
    MANAGE_CHANNELS =              1 << 4
    MANAGE_GUILD =                 1 << 5
    ADD_REACTIONS =                1 << 6
    VIEW_AUDIT_LOG =               1 << 7
    PRIORITY_SPEAKER =             1 << 8
    STREAM =                       1 << 9
    VIEW_CHANNEL =                 1 << 10
    SEND_MESSAGES =                1 << 11
    SEND_TTS_MESSAGES =            1 << 12
    MANAGE_MESSAGES =              1 << 13
    EMBED_LINKS =                  1 << 14
    ATTACH_FILES =                 1 << 15
    READ_MESSAGE_HISTORY =         1 << 16
    MENTION_EVERYONE =             1 << 17
    USE_EXTERNAL_EMOJIS =          1 << 18
    VIEW_GUILD_INSIGHTS =          1 << 19
    CONNECT =                      1 << 20
    SPEAK =                        1 << 21
    MUTE_MEMBERS =                 1 << 22
    DEAFEN_MEMBERS =               1 << 23
    MOVE_MEMBERS =                 1 << 24
    USE_VAD =                      1 << 25
    CHANGE_NICKNAME =              1 << 26
    MANAGE_NICKNAMES =             1 << 27
    MANAGE_ROLES =                 1 << 28
    MANAGE_WEBHOOKS =              1 << 29
    MANAGE_EMOJIS_AND_STICKERS =   1 << 30
    USE_APPLICATION_COMMANDS =     1 << 31
    REQUEST_TO_SPEAK =             1 << 32
    MANAGE_THREADS =               1 << 34
    CREATE_PUBLIC_THREADS =        1 << 35
    CREATE_PRIVATE_THREADS =       1 << 36
    USE_EXTERNAL_STICKERS =        1 << 37
    SEND_MESSAGES_IN_THREADS =     1 << 38
    START_EMBEDDED_ACTIVITIES =    1 << 39

    def any(permissions: int, any_permissions: Permissions, /):
        return (permissions & any_permissions) == any_permissions


class AccessToken(object):
    def __init__(self, data: dict) -> None:
        self.data = data

    @property
    def access_token(self) -> str:
        return self.data.get("access_token")

    @property
    def token_type(self) -> str:
        return self.data.get("token_type")

    @property
    def expires_in(self) -> int:
        return self.data.get("expires_in")

    @property
    def refresh_token(self) -> str:
        return self.data.get("refresh_token")

    @property
    def scope(self) -> str:
        return self.data.get("scope")

    def __repr__(self) -> str:
        return self.access_token


class RefreshToken(AccessToken):
    ...


class Token(AccessToken):
    def __init__(self, data: dict) -> None:
        del AccessToken.refresh_token
        super().__init__(data)


class Guild(object):
    def __init__(self, data: dict) -> None:
        self._data = data
    
    @property
    def id(self) -> str:
        return self._data.get("id")

    @property
    def icon(self) -> str:
        icon_hash: str = self._data.get("icon")
        if not icon_hash:
            return f"https://via.placeholder.com/1024/2c2f33/ffffff?text={self.name[0]}"
        ext = "png"
        if icon_hash.startswith("a_"):
            ext = "gif"
        return f"{IMAGE_BASE}/icons/{self.id}/{icon_hash}.{ext}"
    
    @property
    def name(self) -> str:
        return self._data.get("name")
    
    @property
    def is_owner(self) -> bool:
        return self._data.get("owner")

    @property
    def data(self) -> dict:
        return {"id": self.id, "name": self.name, "icon": self.icon, "is_owner": self.is_owner}

    def __repr__(self) -> str:
        return self.name

class User(object):
    def __init__(self, data: dict, token: str) -> None:
        self.data = data
        self.token = token

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def username(self) -> str:
        return self.data.get("username")

    @property
    def avatar(self) -> str:
        avatar_hash: str = self.data.get("avatar")
        ext = "png"
        if avatar_hash.startswith("a_"):
            ext = "gif"
        return f"{IMAGE_BASE}/avatars/{self.id}/{avatar_hash}.{ext}"

    def get_guild(self, guild_id) -> Guild | None | dict:
        r = request("GET", f"{BASE}/users/@me/guilds",
                    headers={"Authorization": f"Bearer {self.token}"})
        guild = [i for i in r.json() if i["id"] == str(guild_id)]
        if not guild:
            return None
        guild: dict = guild[0]
        if guild["owner"] or Permissions.any(int(guild["permissions"]), Permissions.MANAGE_GUILD):
            return Guild(guild)
        return {"code": 1, "Error": "Missing Permissions"}

    def guilds(self) -> list[Guild]:
        r = request("GET", f"{BASE}/users/@me/guilds",
            headers={"Authorization": f"Bearer {self.token}"})
        x = [guild for guild in r.json() if guild["owner"] or Permissions.any(int(guild["permissions"]), Permissions.ADMINISTRATOR)]
        return [Guild(guild) for guild in x]

class Bot(User):
    def guilds(self) -> list[Guild]:
        r = request("GET", f"{BASE}/users/@me/guilds", headers={"Authorization": f"Bot {self.token}"})
        return [Guild(i) for i in r.json()]

    @property
    def discriminator(self):
        return self.data.get("discriminator")

    def __repr__(self) -> str:
        return f"{self.username}#{self.discriminator}"


@dataclass
class GuildInfo:
    _id: int
    prefix: str
    channel: t.Optional[int]
    time: int
    anti_spam: bool
    embed: bool
    role_id: int


@dataclass
class Channel:
    id: int
    name: str
    type: t.Any


@dataclass
class Role:
    id: int
    name: str

