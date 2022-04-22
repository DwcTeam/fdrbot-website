from flask import Blueprint, redirect, request, session, current_app as app, jsonify
from utlits import Auth, encrypt_token, is_auth
from datetime import datetime

auth = Blueprint("auth", __name__)

@auth.route("/auth/login", methods=["POST"])
def outh():
    auth: Auth = app.auth
    data = request.get_json()
    if not data or not data.get("code"):
        return jsonify({"error": "No code provided"}), 400
    access_token = auth.access_token(data["code"])
    user = auth.user(access_token)
    # insert to logs for admin page
    app.logs.insert_one({"user_id": user.id, "username": user.username, "avatar_url": user.avatar, "type": "login", "time": datetime.now()})
    data = app.logins.find_one({"_id": user.id})
    if not data:
        app.logins.insert_one(user.as_dict)
    else :
        app.logins.update_one({"_id": user.id}, {"$set": user.as_dict})
    token = encrypt_token(access_token.access_token, user.id)
    user_data = user.as_dict
    user = user_data["user"]
    user["id"] = str(user_data["_id"])
    return jsonify({"user": user, "token": token})


@auth.route("/logout")
@is_auth
def logout():

    # app.logs.insert_one({"user_id": user.id, "username": user.username, "avatar_url": user.avatar, "type": "login", "time": datetime.now()})
    return redirect("/")
