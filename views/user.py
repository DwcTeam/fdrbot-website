from flask import Blueprint, jsonify, current_app as app, request
from utlits import is_auth, Auth, is_admin, check_guilds, convert_data_user, decrypt_token
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
    user_data = col_logins.find_one({"_id": user_id})
    user = convert_data_user(user_data)
    guilds = user.guilds()
    alive_guilds = check_guilds(guilds)  # send to cache bot to know if guild is alive
    available_guilds = [i.as_dict for i in guilds if i.id in alive_guilds]
    unavailable_guilds = [i.as_dict for i in guilds if i.id not in alive_guilds]
    return jsonify({"available_guilds": available_guilds, "unavailable_guilds": unavailable_guilds})
    

