from flask import Blueprint, request, jsonify, session, current_app
from utlits import GuildUpdateType, Guild, Azkar, Auth, login_required

api = Blueprint("api", __name__)
auth: Auth = current_app.auth

@api.route("/api")
def api_main():
    return jsonify({"Message": "Hello World, API is work"})

@api.route("/api/guilds", methods=["GET"])
@login_required
def guilds():
    token = session.get("token")
    guilds = auth.user(token).guilds()
    return jsonify([i.data for i in guilds])

@api.route("/api/guilds/<guild_id>", methods=["GET"])
@login_required
def get_guild(guild_id):
    token = session.get("token")
    guild = auth.user(token).get_guild(guild_id)
    if not guild:
        return jsonify({"Error": "Guild Not Found", "code": 0})
    if guild.get("code") == 1:
        return jsonify(guild)
    x = Guild(guild_id)
    if not x.info:
        x.insert()
    return jsonify(x.info)
    




