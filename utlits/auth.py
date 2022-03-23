from requests import request
from .objects import AccessToken, User

BASE = "https://discord.com/api/v9"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}


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
        data = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.REDIRECT_URI.replace("%3A", ":").replace("%2F", "/")
        }
        r = request(
            method="POST", 
            url=f"{BASE}/oauth2/token", 
            data=data, 
            headers=headers
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
            headers={"Authorization": f"Bearer {token.access_token}"}
        )
        data = r.json()
        return User(
            id=int(data["id"]),
            username=data["username"] if len(data["username"]) < 15 else data["username"][:10] + "...",
            avatar=User._convert_avatar(data),
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
            expires_in=token.expires_in,
            refresh_token=token.refresh_token,
            scope=token.scope,
        )

