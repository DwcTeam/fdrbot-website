from flask import Blueprint, request, jsonify


api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/")
def index():
    return jsonify({"message": "Why are you hacker? pls don't hack me!"})

@api.route('/guilds', methods=['GET'])
def guilds():
    return jsonify({"message": "Working on it!"})

@api.route("/guilds/<guild_id>", methods=['GET'])
def guild(guild_id):
    return jsonify({"message": "Working on it!"})

@api.route("/guilds/<guild_id>/quran/channel", methods=['POST'])
def quran_channel(guild_id):
    return jsonify({"message": "Working on it!"})

@api.route("/guilds/<guild_id>/quran/role", methods=['POST'])
def quran_role(guild_id):
    return jsonify({"message": "Working on it!"})

@api.route("/guilds/<guild_id>/time", methods=['POST'])
def time(guild_id):
    return jsonify({"message": "Working on it!"})

@api.route("/guilds/<guild_id>/color", methods=['POST'])
def color(guild_id):
    return jsonify({"message": "Working on it!"})
