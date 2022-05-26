from requests import request
from .objects import AccessToken, User, Guild, Permissions, convert_guild, convert_user, Webhook, WebhookUser
import typing as t

BASE = "https://discord.com/api/v10"


class RestWebhook(object):
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = "Bot " + token

    def create(self, data: t.Dict[str, str]) -> Webhook:
        return Webhook(**request("POST", self.url, headers={"Authorization": self.token}, json=data).json())

    def delete(self):
        return request("DELETE", self.url, headers={"Authorization": self.token})

    def get(self):
        return request("GET", self.url, headers={"Authorization": self.token})

    @classmethod
    def get_webhooks(self, token: str, channel_id: int) -> t.List["Webhook"]:
        res = request(
            "GET",
            f"{BASE}/channels/{channel_id}/webhooks",
            headers={"Authorization": "Bot " + token},
        )
        return [Webhook(**webhook) for webhook in res.json()]

    def __repr__(self) -> str:
        return f"<Webhook url={self.url} token={self.token}>"


class Auth(object):
    def __init__(
        self,
        client_id: int,
        client_secret: str,
        redirect_uri: str,
    ) -> None:
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri

    def access_token(self, code: str) -> AccessToken:
        r = request(
            method="POST",
            url=f"{BASE}/oauth2/token",
            data={
                "client_id": self.CLIENT_ID,
                "client_secret": self.CLIENT_SECRET,
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": self.REDIRECT_URI.replace("%3A", ":").replace(
                    "%2F", "/"
                ),
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        r.raise_for_status()
        data = r.json()
        return AccessToken(
            access_token=data["access_token"],
            token_type=data["token_type"],
            expires_in=data["expires_in"],
            refresh_token=data["refresh_token"],
            scope=data["scope"],
        )

    def refresh_token(self, token: AccessToken) -> AccessToken:
        r = request(
            method="POST",
            url=f"{BASE}/oauth2/token",
            data={
                "client_id": self.CLIENT_ID,
                "client_secret": self.CLIENT_SECRET,
                "grant_type": "refresh_token",
                "refresh_token": token.refresh_token,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        r.raise_for_status()
        data = r.json()
        return AccessToken(
            access_token=data["access_token"],
            token_type=data["token_type"],
            expires_in=data["expires_in"],
            refresh_token=data["refresh_token"],
            scope=data["scope"],
        )

    def user(self, token: AccessToken) -> User:
        r = request(
            method="GET",
            url=f"{BASE}/users/@me",
            headers={"Authorization": f"Bearer {token.access_token}"},
        )
        data = r.json()
        return convert_user(token, data, int(data["id"]))

    def get_guild(
        self, token: AccessToken, guild_id
    ) -> t.Optional[t.Union[Guild, dict]]:
        r = request(
            method="GET",
            url=f"{BASE}/users/@me/guilds",
            headers={"Authorization": f"Bearer {token.access_token}"},
        )
        guild = [i for i in r.json() if i["id"] == str(guild_id)]
        # check if guild is found
        if not guild:
            return None
        guild: dict = guild[0]
        # check if user owner or admin
        if guild["owner"] or Permissions.any(
            int(guild["permissions"]), Permissions.MANAGE_GUILD
        ):
            return convert_guild(guild)
        return {"code": 1, "Error": "Missing Permissions"}  # missing permissions

    def guilds(self, token: AccessToken) -> t.List[Guild]:
        r = request(
            method="GET",
            url=f"{BASE}/users/@me/guilds",
            headers={"Authorization": f"Bearer {token.access_token}"},
        )
        x = [
            guild
            for guild in r.json()
            if guild["owner"]
            or Permissions.any(int(guild["permissions"]), Permissions.ADMINISTRATOR)
        ]
        return [convert_guild(guild) for guild in x]
