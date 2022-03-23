from flask import Blueprint, request, jsonify, current_app as app, session
from utlits import login_required, send_ping, Auth, AccessToken, check_permission, get_guild as get_guild_api


api = Blueprint("api", __name__, url_prefix="/api")

auth = Auth(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'], app.config['REDIRECT_URI'])

@api.route("/")
def index():
    return jsonify({"message": "Why are you hacker? pls don't hack me!"})

@api.route("/ping")
def ping():
    return jsonify({"stats": send_ping()})

@api.route("/guilds/<int:guild_id>/update", methods=["POST"])
@login_required
def update_guild(guild_id: int):
    user = auth.user(AccessToken(**app.logins.find_one({"token.access_token": session["token"]}).get("token")))
    guild = user.get_guild(guild_id)
    
    if not guild:
        return jsonify({"message": "You are not hava access to this guild!"}), 403

    data = request.get_json()

    if not data:
        return jsonify({"message": "No data sent"}), 400

    print(data)
    # cehck values
    if (not data.get("anti_spam") or not data.get("embed") or \
        not data.get("role_id") or not data.get("channel") or not data.get("time")):
        return jsonify({"message": "Missing values"}), 400
    
    # chcek values type
    if not isinstance(data.get("anti_spam"), bool) or not isinstance(data.get("embed"), bool) or \
        not isinstance(data.get("role_id"), int) or not isinstance(data.get("channel"), int) or not isinstance(data.get("time"), int):
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
    if data.get("channel_id") not in [i.id for i in guild.channels]:
        return jsonify({"message": "Invalid channel"}), 400
    
    # check if role is valid
    if data.get("role_id") not in [i.id for i in guild.roles]:
        return jsonify({"message": "Invalid role"}), 400

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
