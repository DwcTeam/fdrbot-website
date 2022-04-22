import base64
import typing as t

def encrypt_token(access_token: str, user_id: t.Union[int, str]) -> str:
    length = access_token.__len__() / 2
    token = base64.b64encode(str(user_id).encode()).decode() + "." + access_token[:int(length)]
    return token

def decrypt_token(token: str) -> t.Tuple[str, int]:
    access_token = token.split(".")[1]
    user_id = int(base64.b64decode(token.split(".")[0]).decode())
    return user_id, access_token
