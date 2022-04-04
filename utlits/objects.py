from __future__ import annotations
from dataclasses import dataclass
import typing as t
from flask import current_app as app
from datetime import datetime

BASE = "https://discord.com/api/v9"
IMAGE_BASE = "https://cdn.discordapp.com"

def convert_icon_hash(data: dict) -> str:
    icon_hash: str = data.get("icon")
    if not icon_hash:
        return f"https://via.placeholder.com/1024/2c2f33/ffffff?text={data['name'][0]}"
    return f"{IMAGE_BASE}/icons/{data['id']}/{icon_hash}.{'gif' if icon_hash.startswith('a_') else 'png'}"

def convert_guild(data: dict) -> Guild:
    return Guild(
        id=int(data.get("id")),
        name=data.get("name"),
        icon=convert_icon_hash(data),
        is_icon=True if data.get("icon") else False,
        is_owner=data.get("owner"),
        permissions=int(data.get("permissions")),
        features=data.get("features"),
        as_dict=data
    )

def convert_avatar(data: dict) -> str:
    avatar_hash = data.get("avatar", None)
    if not avatar_hash:
        return f"{IMAGE_BASE}/embed/avatars/{int(data.get('discriminator')) % 5}.png"
    return f"{IMAGE_BASE}/avatars/{data.get('id')}/{avatar_hash}.{'gif' if avatar_hash.startswith('a_') else 'png'}"

def convert_channels(channels: t.List[t.Dict]) -> t.List[Channel]:
    return [Channel(**channel) for channel in channels]

def convert_roles(roles: t.List[t.Dict]) -> t.List[Role]:
    return [Role(**role) for role in roles]

def convert_user(token: AccessToken, data: dict, user_id: int) -> User:
    return User(
        id=user_id,
        username=data["username"] if len(data["username"]) < 15 else data["username"][:10] + "...",
        avatar=convert_avatar(data) if not data["avatar"].startswith(IMAGE_BASE) else data["avatar"],
        discriminator=int(data["discriminator"]),
        public_flags=data["public_flags"],
        flags=data["flags"],
        banner=data["banner"],
        banner_color=data["banner_color"],
        accent_color=data["accent_color"],
        locale=data["locale"],
        mfa_enabled=data["mfa_enabled"],
        email=data["email"],
        verified=data["verified"],
        token=token.access_token,
        token_type=token.token_type,
        expires_in=token.expires_in if isinstance(token.expires_in, datetime) else datetime.fromtimestamp(datetime.now().timestamp() + token.expires_in),
        refresh_token=token.refresh_token,
        scope=token.scope
    )

def convert_token(data: dict) -> AccessToken:
    return AccessToken(**data["token"])

def convert_data_user(data: dict) -> User:
    return convert_user(convert_token(data), data.get("user"), data.get("_id"))

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
    expires_in: t.Union[int, datetime]
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
class BotGuild:
    channels: t.List[Channel]
    roles: t.List[Role]


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
    email: str
    verified: bool
    token: str
    token_type: str
    expires_in: datetime
    refresh_token: str
    scope: t.Union[t.List[str], str]

    @property
    def as_dict(self) -> dict:
        return {
            "_id": self.id,
            "user": {
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
                "email": self.email,
                "verified": self.verified
            },
            "token": {
                "access_token": self.token,
                "token_type": self.token_type,
                "expires_in": self.expires_in,
                "refresh_token": self.refresh_token,
                "scope": self.scope
            },
        } 

    @property
    def access_token(self) -> AccessToken:
        return convert_token(self.as_dict)

    def guilds(self) -> t.List[Guild]:
        return app.auth.guilds(self.access_token)
    
    def get_guild(self, guild_id: int) -> Guild:
        return app.auth.get_guild(self.access_token, guild_id)
