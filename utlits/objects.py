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

@dataclass
class AccessToken:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str


@dataclass
class Guild:
    id: int
    name: str
    icon: str
    is_icon: bool
    is_owner: bool
    permissions: int
    features: t.List[str]
    as_dict: dict


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


@dataclass
class User:
    id: int
    username: str
    avatar: str
    discriminator: int
    public_flags: int
    flags: int
    banner: t.Any
    banner_color: t.Any
    accent_color: t.Any
    locale: str
    mfa_enabled: bool
    token: str
    email: str
    verified: bool

    @property
    def as_dict(self) -> dict:
        return {
            "_id": self.id,
            "username": self.username,
            "avatar": self.avatar,
            "discriminator": self.discriminator,
            "public_flags": self.public_flags,
            "flags": self.flags,
            "banner": self.banner,
            "banner_color": self.banner_color,
            "accent_color": self.accent_color,
            "locale": self.locale,
            "mfa_enabled": self.mfa_enabled,
            "token": self.token,
            "email": self.email,
            "verified": self.verified
        }

    @staticmethod
    def _convert_avatar(id: int, avatar_hash: str) -> str:
        return f"{IMAGE_BASE}/avatars/{id}/{avatar_hash}.{'gif' if avatar_hash.startswith('a_') else 'png'}" 

    def _convert_icon_hash(self, data: dict) -> str:
        icon_hash: str = data.get("icon")
        if not icon_hash:
            return f"https://via.placeholder.com/1024/2c2f33/ffffff?text={data['name'][0]}"
        return f"{IMAGE_BASE}/icons/{data['id']}/{icon_hash}.{'gif' if icon_hash.startswith('a_') else 'png'}"

    def _convert_guild(self, data: dict) -> Guild:
        return Guild(
            id=int(data.get("id")),
            name=data.get("name"),
            icon=self._convert_icon_hash(data),
            is_icon=True if data.get("icon") else False,
            is_owner=data.get("owner"),
            permissions=int(data.get("permissions")),
            features=data.get("features"),
            as_dict=data
        )

    def get_guild(self, guild_id) -> Guild | None | dict:
        r = request(
            method="GET", 
            url=f"{BASE}/users/@me/guilds",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        guild = [i for i in r.json() if i["id"] == str(guild_id)]
        # check if guild is found
        if not guild:
            return None
        guild: dict = guild[0]
        # check if user owner or admin
        if guild["owner"] or Permissions.any(int(guild["permissions"]), Permissions.MANAGE_GUILD):
            return self._convert_guild(guild)
        return {"code": 1, "Error": "Missing Permissions"}  # missing permissions

    def guilds(self) -> list[Guild]:
        r = request(
            method="GET", 
            url=f"{BASE}/users/@me/guilds",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        x = [guild for guild in r.json() if guild["owner"] or Permissions.any(int(guild["permissions"]), Permissions.ADMINISTRATOR)]
        return [self._convert_guild(guild) for guild in x]


