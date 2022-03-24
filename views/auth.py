from flask import Blueprint, redirect, request, session, current_app as app
from utlits import Auth

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    if "token" in session:
        return redirect(request.args.get("next", "/"))
    return redirect(app.config['REDIRECT_URL'])

@auth.route('/outh')
def outh():
    auth: Auth = app.auth
    if "token" in session:
        return redirect("/dashboard")
    access_token = auth.access_token(request.args.get('code'))
    session['token'] = access_token.access_token
    user = auth.user(access_token)
    data = app.logins.find_one({"_id": user.id})
    if not data:
        app.logins.insert_one(user.as_dict)
    else :
        app.logins.update_one({"_id": user.id}, {"$set": user.as_dict})
    return redirect("/dashboard")

@auth.route("/auth_guild")
def auth_guild():
    args = request.args
    return redirect(f"/dashboard/{args.get('guild_id')}")


@auth.route('/logout')
def logout():
    session.clear()
    return redirect("/")
