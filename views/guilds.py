from __future__ import annotations
from flask import Blueprint, request, jsonify, current_app as app, session
import typing as t
from utlits import (
    send_ping, 
    Auth, 
    convert_data_user, 
    check_permission, 
    get_guild as get_guild_api, 
    get_guild_info,
    is_auth
)
from utlits.encrypt import decrypt_token


guilds = Blueprint("api", __name__, url_prefix="/guilds")

auth: Auth = app.auth

@guilds.route("/")
def index():
    return jsonify({"message": "Why are you hacker? pls don't hack me!"})

@guilds.route("/ping")
def ping():
    return jsonify({"stats": send_ping()})

@guilds.route("/<int:guild_id>/update", methods=["POST"])
@is_auth
def update_guild(guild_id: int):
    authorization = request.headers.get('Authorization')
    print(authorization)
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
    if int(data.get("time")) not in [1800, 3600, 7200, 21600, 28800, 43200, 86400]:
        return jsonify({"message": "Invalid time"}), 400

    info = app.db.find_one({"_id": guild_id})
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

    app.db.update_one({"_id": guild_id}, {"$set": data}, upsert=True)
    return jsonify({"message": "Success!"})


@guilds.route("/<int:guild_id>", methods=["GET"])
@is_auth
def get_guild(guild_id: int):
    info = app.db.find_one({'_id': guild_id})
    if not info:
        return jsonify({"error": "Guild not found"}), 404
    del info["_id"]
    del info["prefix"]
    del info["webhook_url"]
    info["channel"] = str(info.get("channel")) if info.get("channel") else None
    info["role_id"] = str(info.get("role_id")) if info.get("role_id") else None
    info["time"] = str(info.get("time")) if info.get("time") else None
    guild = get_guild_api(guild_id)
    
    # remove everyone role
    del guild.roles[0]
    data = {
        "guild": guild,
        "info": info
    }
    return jsonify(data)


@guilds.route("/<int:guild_id>/info", methods=["GET"])
def get_guild_admin(guild_id: int):
    info = app.db.find_one({'_id': guild_id})
    guild = get_guild_info(guild_id)
    if not guild["status"]:
        return jsonify({"error": "Guild not found"}), 404
    data = {}
    data.update(guild["guild"])
    del info["_id"]
    del info["prefix"]
    del info["webhook_url"]
    info["channel"] = str(info.get("channel")) if info.get("channel") else None
    info["role_id"] = str(info.get("role_id")) if info.get("role_id") else None
    info["time"] = str(info.get("time")) if info.get("time") else None
    data.update(info)
    return jsonify(data)
