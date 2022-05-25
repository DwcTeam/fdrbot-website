from flask import Blueprint, jsonify, current_app as app, request
from redis import Redis
from utlits import is_auth, is_admin, convert_data_user, decrypt_token
from pymongo.collection import Collection


user = Blueprint('user', __name__, url_prefix='/user')



@user.route('/@me')
@is_auth
def user_data():
    authorization = request.headers.get('Authorization')
    token = authorization.split(' ')[1]
    user_id, access_token = decrypt_token(token)
    with app.app_context():
        col_logins: Collection = app.col_logins
    user_data = col_logins.find_one({"_id": user_id})
    user = convert_data_user(user_data).as_dict["user"]
    if is_admin(user_id):
        user["admin"] = True
    return jsonify(user)


@user.route('/@me/guilds')
@is_auth
def user_guilds():
    authorization = request.headers.get('Authorization')
    token = authorization.split(' ')[1]
    user_id, access_token = decrypt_token(token)
    with app.app_context():
        col_logins: Collection = app.col_logins
        redis: Redis = app.redis
    user_data = col_logins.find_one({"_id": user_id})
    user = convert_data_user(user_data)
    guilds = user.guilds()
    alive_guilds = filter(lambda guild: True if redis.get(f"guild:{guild.id}") else False, guilds)
    ids = [g.id for g in list(alive_guilds)]
    available_guilds = [i.as_dict for i in guilds if i.id in ids]
    unavailable_guilds = [i.as_dict for i in guilds if i.id not in ids]
    return jsonify({"available_guilds": available_guilds, "unavailable_guilds": unavailable_guilds})
    

