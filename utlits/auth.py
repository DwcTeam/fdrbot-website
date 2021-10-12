from flask.json import jsonify
from requests import request
from ._objects import AccessToken, RefreshToken, Token, User, Bot

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
        self.SCOPE = "identify+guilds+email"

    def access_token(self, code: str) -> AccessToken:
        data = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.REDIRECT_URI
        }
        r = request("POST", f"{BASE}/oauth2/token", data=data, headers=headers)
        r.raise_for_status()
        return AccessToken(r.json())

    def refresh_token(self, refresh_token: str) -> RefreshToken:
        data = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        r = request("POST", f"{BASE}/oauth2/token", data=data, headers=headers)
        r.raise_for_status()
        return RefreshToken(r.json())

    def get_token(self) -> Token:
        data = {
            "grant_type": "client_credentials",
            "scope": "identify connections"
        }
        r = request("POST", f"{BASE}/oauth2/token", data=data,
                    headers=headers, auth=(self.CLIENT_ID, self.CLIENT_SECRET))
        r.raise_for_status()
        return Token(r.json())

    def user(self, token: str) -> User:
        r = request("GET", f"{BASE}/users/@me",
                    headers={"Authorization": f"Bearer {token}"})
        return User(r.json(), token)

    def bot(self, bot_token: str) -> Bot:
        r = request("GET", f"{BASE}/users/@me",
                    headers={"Authorization": f"Bot {bot_token}"})
        r.raise_for_status()
        return r.json()
