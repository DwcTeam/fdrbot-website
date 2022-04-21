from flask import Blueprint, jsonify, render_template, current_app as app, session, abort, request
from utlits import is_auth, Auth, get_guild, is_admin, check_guilds
from utlits import check_permission, get_guild_info, convert_data_user
from flask_jwt_extended import decode_token

user = Blueprint('user', __name__, url_prefix='/user')

auth: Auth = app.auth


@user.route('/@me')
@is_auth
def user_data():
    authorization = request.headers.get('Authorization')
    token = authorization.split(' ')[1]
    user_id = decode_token(token).get("sub").get("user_id")
    user_data = app.logins.find_one({"_id": user_id})
    if not user_data:
        return jsonify({"error": "User not found"}), 400
    user = user_data["user"]
    user["id"] = str(user_data["_id"])
    if is_admin(user_id):
        user["admin"] = True
    return jsonify(user)


@user.route('/@me/guilds')
@is_auth
def user_guilds():
    authorization = request.headers.get('Authorization')
    token = authorization.split(' ')[1]
    user_id = decode_token(token).get("sub").get("user_id")
    user_data = app.logins.find_one({"_id": user_id})
    if not user_data:
        return jsonify({"error": "User not found"}), 400
    user = convert_data_user(user_data)
    guilds = user.guilds()
    alive_guilds = check_guilds(guilds)  # send to cache bot to know if guild is alive
    available_guilds = [i.as_dict for i in guilds if i.id in alive_guilds]
    unavailable_guilds = [i.as_dict for i in guilds if i.id not in alive_guilds]
    return jsonify({"available_guilds": available_guilds, "unavailable_guilds": unavailable_guilds})
    

