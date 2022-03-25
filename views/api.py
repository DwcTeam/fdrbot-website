from flask import Blueprint, request, jsonify, current_app as app, session
from utlits import login_required, send_ping, Auth, convert_data_user, check_permission, get_guild as get_guild_api
import typing as t
from utlits.checks import only_admin
from utlits.local_api import get_guild_info

from utlits.objects import AccessToken


api = Blueprint("api", __name__, url_prefix="/api")

auth: Auth = app.auth

@api.route("/")
def index():
    return jsonify({"message": "Why are you hacker? pls don't hack me!"})

@api.route("/ping")
def ping():
    return jsonify({"stats": send_ping()})

@api.route("/guilds/<int:guild_id>/update", methods=["POST"])
@login_required
def update_guild(guild_id: int):
    user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
    guild = user.get_guild(guild_id)
    
    if not guild:
        return jsonify({"message": "You are not hava access to this guild!"}), 403

    data: t.Optional[t.Dict] = request.get_json()

    if not data:
        return jsonify({"message": "No data sent"}), 400

    # cehck values
    keys = ["channel", "time", "anti_spam", "embed", "role_id"]
    if keys != list(data.keys()):
        return jsonify({"message": "Missing values"}), 400
    
    # chcek values type
    if not isinstance(data.get("anti_spam"), bool) or not isinstance(data.get("embed"), bool) or \
        not isinstance(data.get("role_id"), t.Optional[str]) or not isinstance(data.get("channel"), t.Optional[str]) or not isinstance(data.get("time"), int):
        return jsonify({"message": "Invalid values"}), 400
    
    # check values range
    if data.get("time") not in [1800, 3600, 7200, 21600, 28800, 43200, 86400]:
        return jsonify({"message": "Invalid time"}), 400

    info = app.db.find_one({"_id": guild_id})
    del info["_id"]
    del info["prefix"]

    # check if not make updates
    if info == data:
        return jsonify({"message": "No updates"}), 400

    guild = get_guild_api(guild_id)

    # check if channel is valid
    if data.get("channel") and data.get("channel") not in [i.id for i in guild.channels]:
        return jsonify({"message": "Invalid channel"}), 400
    
    # check if role is valid
    if data.get("role_id") and data.get("role_id") not in [i.id for i in guild.roles]:
        return jsonify({"message": "Invalid role"}), 400


    data["channel"] = data.get("channel")

    app.db.update_one({"_id": guild_id}, {"$set": data}, upsert=True)
    return jsonify({"message": "Success!"})

@api.route("/guilds/<int:guild_id>/info", methods=["GET"])
@login_required
@check_permission
def get_guild(guild_id: int):
    guild = app.db.find_one({'_id': guild_id})
    if not guild:
        return jsonify({"error": "Guild not found"}), 404
    del guild["_id"]
    del guild["prefix"]
    data = {
        "status": True if guild else False,
        "guild": guild
    }
    return jsonify(data)


@api.route("/guilds/<int:guild_id>/info/admin", methods=["GET"])
@login_required
@only_admin
def get_guild_admin(guild_id: int):
    info = app.db.find_one({'_id': guild_id})
    guild = get_guild_info(guild_id)
    if not guild:
        return jsonify({"error": "Guild not found"}), 404
    return jsonify({
        "status": True if guild["status"] else False,
        "guild": guild,
        "info": info
    })