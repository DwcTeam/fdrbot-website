from __future__ import annotations
import json
from flask import Blueprint, request, jsonify, current_app as app
import typing as t

from redis import Redis
from utlits import (
    convert_data_user,  
    get_guild as get_guild_api, 
    get_guild_info,
    is_auth
)
from utlits.encrypt import decrypt_token
from pymongo.collection import Collection

from utlits.objects import convert_roles

guilds = Blueprint("api", __name__, url_prefix="/guilds")

@guilds.route("/")
def index():
    return jsonify({"message": "Why are you hacker? pls don't hack me!"})


@guilds.route("/<int:guild_id>/update", methods=["POST"])
@is_auth
def update_guild(guild_id: int):
    authorization = request.headers.get('Authorization')
    type_token, token = authorization.split(' ')[0], authorization.split(' ')[1]
    user_id, access_token = decrypt_token(token)
    user_data = app.logins.find_one({"_id": user_id})
    user = convert_data_user(user_data)
    guild = user.get_guild(guild_id)
    
    if not guild:
        return jsonify({"message": "You are not hava access to this guild!"}), 403

    data: t.Optional[t.Dict] = request.get_json()

    if not data:
        return jsonify({"message": "No data sent"}), 400

    # cehck values
    keys = ["channel", "time", "anti_spam", "embed", "role_id"]
    if (False in [True for i in list(data.keys()) if i in keys]) and len(data.keys()) != len(keys):
        return jsonify({"message": "Missing values"}), 400
    # chcek values type
    if not isinstance(data.get("anti_spam"), bool) or not isinstance(data.get("embed"), bool) or \
        not (isinstance(data.get("role_id"), str) or data.get("role_id") is None) or \
        not (isinstance(data.get("channel"), str) or data.get("channel") is None) or \
        not data.get("time").isdigit():
        return jsonify({"message": "Invalid values"}), 400
    
    # check values range
    if int(data.get("time")) not in [1800, 3600, 7200, 21600, 43200, 86400]:
        return jsonify({"message": "Invalid time"}), 400

    with app.app_context():
        db: Collection = app.col_guilds

    info = db.find_one({"_id": guild_id})
    for key in list(info.keys()):
        if key not in keys:
            info.pop(key)

    data["channel"] = int(data.get("channel")) if data.get("channel") else None
    data["role_id"] = int(data.get("role_id")) if data.get("role_id") else None
    # check if not make updates
    if info == data:
        return jsonify({"message": "No updates"}), 400

    guild = get_guild_api(guild_id)

    # check if channel is valid
    if data.get("channel") and str(data.get("channel")) not in [i.id for i in guild.channels]:
        return jsonify({"message": "Invalid channel"}), 400
    
    # check if role is valid
    if data.get("role_id") and str(data.get("role_id")) not in [i.id for i in guild.roles]:
        return jsonify({"message": "Invalid role"}), 400

    db.update_one({"_id": guild_id}, {"$set": data}, upsert=True)
    return jsonify({"message": "Success!"})


# @guilds.route("/<int:guild_id>", methods=["GET"])
# @is_auth
# def get_guild(guild_id: int):
#     with app.app_context():
#         db: Collection = app.col_guilds
#         redis: Redis = app.redis

#     info = db.find_one({'_id': guild_id})
#     if not info:
#         return jsonify({"error": "Guild not found"}), 404
#     del info["_id"]
#     del info["webhook"]
#     info["channel_id"] = str(info.get("channel_id")) if info.get("channel_id") else None
#     info["role_id"] = str(info.get("role_id")) if info.get("role_id") else None
#     info["time"] = str(info.get("time")) if info.get("time") else None
#     guild = json.loads(redis.get(f"guild:{guild_id}"))
#     roles = convert_roles(guild["roles"])
#     channels = guild["channels"]    
#     # remove everyone role
#     del guild.roles[0]
#     data = {
#         "guild": {
#             "roles": roles,
#             "channels": channels
#         },
#         "info": info
#     }
#     return jsonify(data)


@guilds.route("/<int:guild_id>", methods=["GET"])
@is_auth
def get_guild_admin(guild_id: int):
    with app.app_context():
        db: Collection = app.col_guilds
        redis: Redis = app.redis
    info = db.find_one({'_id': guild_id})
    guild = json.loads(redis.get(f"guild:{guild_id}"))
    if not guild:
        return jsonify({"error": "Guild not found"}), 404
    data = {}
    del guild["roles"][0]
    data.update(guild)
    del info["_id"]
    del info["webhook"]
    info["channel_id"] = str(info.get("channel_id")) if info.get("channel_id") else None
    info["role_id"] = str(info.get("role_id")) if info.get("role_id") else None
    info["time"] = str(info.get("time")) if info.get("time") else None
    data.update(info)
    return jsonify(data)
