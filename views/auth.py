from flask import Blueprint, redirect, request, session, current_app
from utlits import Auth

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if "token" in session:
        return redirect(request.args.get("next", "/"))
    return redirect(current_app.config['REDIRECT_URL'])

@auth.route('/outh')
def outh():
    if "token" in session:
        return redirect("/dashboard")
    auth = Auth(current_app.config['CLIENT_ID'], current_app.config['CLIENT_SECRET'], current_app.config['REDIRECT_URI'])
    access_token = auth.access_token(request.args.get('code'))
    session['token'] = access_token.access_token
    user = auth.user(access_token)
    data = current_app.logins.find_one({"_id": user.id})
    if not data:
        current_app.logins.insert_one(user.as_dict)
    else :
        current_app.logins.update_one({"_id": user.id}, {"$set": user.as_dict})
    return redirect("/dashboard")


@auth.route('/logout')
def logout():
    session.clear()
    return redirect("/")
