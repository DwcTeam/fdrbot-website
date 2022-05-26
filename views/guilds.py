from flask import Blueprint, request, jsonify, current_app as app
import json
import typing as t
from utlits import convert_data_user, is_auth
from utlits.encrypt import decrypt_token
from pymongo.collection import Collection
from redis import Redis
from utlits.objects import Channel, Role, convert_guild, BotGuild
from utlits.rest import RestWebhook, Webhook

guilds = Blueprint("guilds", __name__, url_prefix="/guilds")

@guilds.route("/")
def index():
    return jsonify({"message": "Why are you hacker? pls don't hack me!"})


@guilds.route("/<int:guild_id>/update", methods=["POST"])
@is_auth
def update_guild(guild_id: int):
    authorization = request.headers.get('Authorization')
    type_token, token = authorization.split(' ')[0], authorization.split(' ')[1]
    user_id, access_token = decrypt_token(token)
    with app.app_context():
        db: Collection = app.col_guilds
        redis: Redis = app.redis
        logins: Collection = app.col_logins
    user_data = logins.find_one({"_id": user_id})
    user = convert_data_user(user_data)
    guild = user.get_guild(guild_id)
    
    if not guild:
        return jsonify({"message": "You are not hava access to this guild!"}), 403

    data: t.Optional[t.Dict] = request.get_json()

    if not data:
        return jsonify({"message": "No data sent"}), 400

    # cehck values
    keys = ["channel_id", "time", "embed", "role_id"]
    if (False in [True for i in list(data.keys()) if i in keys]) and len(data.keys()) != len(keys):
        return jsonify({"message": "Missing values"}), 400
    # chcek values type
    if not isinstance(data.get("embed"), bool) or \
        not (isinstance(data.get("role_id"), str) or data.get("role_id") is None) or \
        not (isinstance(data.get("channel_id"), str) or data.get("channel_id") is None) or \
        not data.get("time").isdigit():
        return jsonify({"message": "Invalid values"}), 400
    
    # check values range
    if int(data.get("time")) not in [1800, 3600, 7200, 21600, 43200, 86400]:
        return jsonify({"message": "Invalid time"}), 400

    info = db.find_one({"_id": guild_id})
    for key in list(info.keys()):
        if key not in keys:
            info.pop(key)

    data["channel_id"] = int(data.get("channel_id")) if data.get("channel_id") else None
    data["role_id"] = int(data.get("role_id")) if data.get("role_id") else None
    # check if not make updates
    if info == data:
        return jsonify({"message": "No updates"}), 400

    guild_data = json.loads(redis.get(f"guild:{guild_id}"))
    guild = BotGuild(
        channels=[Channel(**channel) for channel in guild_data["channels"]], 
        roles=[Role(**role) for role in guild_data["roles"]]
    )
    # check if channel is valid
    if data.get("channel_id") and str(data.get("channel_id")) not in [i.id for i in guild.channels]:
        return jsonify({"message": "Invalid channel"}), 400
    
    # check if role is valid
    if data.get("role_id") and str(data.get("role_id")) not in [i.id for i in guild.roles]:
        return jsonify({"message": "Invalid role"}), 400
    
    webhook_data = {}

    if data["channel_id"] and info["channel_id"] != data["channel_id"]:
        channel_webhooks = RestWebhook.get_webhooks(app.config["TOKEN"], int(data["channel_id"]))
        bot_webhooks = list(filter(lambda i: (i.name == "فاذكروني" and int(i.get_user().id) == app.config["CLIENT_ID"]) , channel_webhooks))
        if not bot_webhooks:
            webhook = RestWebhook.create(app.config["TOKEN"], data["channel_id"], "فاذكروني", "https://i.imgur.com/djbP3Zz.png")
            webhook_data = {
                "id": int(webhook.id),
                "token": webhook.token
            }
        else :
            webhook_data = {
                "id": int(bot_webhooks[0].id),
                "token": bot_webhooks[0].token
            }
    
    new_data = {
        "channel_id": data["channel_id"] if (data["channel_id"] != "0") else None,
        "time": int(data["time"]),
        "embed": data["embed"],
        "role_id": data["role_id"] if (data["role_id"] != "0") else None,
        "webhook": webhook_data
    }
    db.update_one({"_id": guild_id}, {"$set": new_data}, upsert=True)
    return jsonify({"message": "Success!"})

@guilds.route("/<int:guild_id>", methods=["GET"])
@is_auth
def get_guild(guild_id: int):
    with app.app_context():
        db: Collection = app.col_guilds
        redis: Redis = app.redis
    info = db.find_one({'_id': guild_id})
    guild = json.loads(redis.get(f"guild:{guild_id}") or "{}")
    if not guild:
        return jsonify({"error": "Guild not found"}), 404
    data = {}
    del guild["roles"][0]
    data.update(guild)
    del info["_id"]
    del info["webhook"]
    info["channel_id"] = str(info.get("channel_id")) if info.get("channel_id") else "0"
    info["role_id"] = str(info.get("role_id")) if info.get("role_id") else "0"
    info["time"] = str(info.get("time")) if info.get("time") else None
    data.update(info)
    return jsonify(data)
