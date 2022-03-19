from flask import Blueprint, request, jsonify, current_app
from utlits import login_required, send_ping, check_permission
from requests import post
from utlits import get_guild_channels
import typing as t

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/")
def index():
    return jsonify({"message": "Why are you hacker? pls don't hack me!"})

@api.route("/ping")
def ping():
    return jsonify({"stats": send_ping()})

@api.route("/guilds/<int:guild_id>/channel", methods=["POST"])
@login_required
@check_permission
def guild_channel(guild_id: int):
    channel_id = request.form.get("channel_id", None)
    try:
        channel_id = int(channel_id) if channel_id else None

        print(channel_id, type(channel_id))

        channels = get_guild_channels(guild_id)

        # search to see if the channel is in the guild
        if channel_id and channel_id not in [i.id for i in channels]:
            return jsonify({"error": "Channel not found"}), 404
    except ValueError:
        return jsonify({"error": "Invalid object type"}), 400
        

    channel_id = int(request.form.get("channel_id")) if request.form.get("channel_id") else None
    res = post(f"{current_app.config['BOT_SERVER']}/update_channel/{guild_id}", json={"channel_id": channel_id})
    return jsonify({"channel_id": res.json()["channel_id"]})

@api.route("/guilds/<int:guild_id>/quran/channel", methods=['POST'])
@login_required
@check_permission
def quran_channel(guild_id):
    data = request.get_json()
    res = post(f"{current_app.config['BOT_SERVER']}/quran_channel/{guild_id}", json={'channel_id': data['channel_id']})
    return jsonify({"channel_id": res.json()["channel_id"]})

@api.route("/guilds/<guild_id>/quran/role", methods=['POST'])
@login_required
@check_permission
def quran_role(guild_id):
    data = request.get_json()
    res = post(f"{current_app.config['BOT_SERVER']}/update_role/{guild_id}", json={'role_id': data['role_id']})
    return jsonify({"role_id": res.json()["role_id"]})

@api.route("/guilds/<guild_id>/time", methods=['POST'])
@login_required
@check_permission
def time(guild_id):
    data = request.get_json()
    res = post(f"{current_app.config['BOT_SERVER']}/update_time/{guild_id}", json={'time': data['time']})
    return jsonify({"time": res.json()["time"]})

@api.route("/guilds/<guild_id>/color", methods=['POST'])
@login_required
@check_permission
def color(guild_id):
    data = request.get_json()
    res = post(f"{current_app.config['BOT_SERVER']}/update_color/{guild_id}", json={'color': data['color']})
    return jsonify({"color": res.json()["color"]})

@api.route("/guilds/<guild_id>/anti_spam", methods=['POST'])
@login_required
@check_permission
def anti_spam(guild_id):
    data = request.get_json()
    res = post(f"{current_app.config['BOT_SERVER']}/update_anti_spam/{guild_id}", json={'anti_spam': data['anti_spam']})
    return jsonify({"anti_spam": res.json()["anti_spam"]})

@api.route("/guilds/<guild_id>/embed", methods=['POST'])
@login_required
@check_permission
def embed(guild_id):
    data = request.get_json()
    res = post(f"{current_app.config['BOT_SERVER']}/update_embed/{guild_id}", json={'embed': data['embed']})
    return jsonify({"embed": res.json()["embed"]})
