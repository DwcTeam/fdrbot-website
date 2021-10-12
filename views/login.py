from flask import Blueprint, session, redirect, request, current_app
from utlits import Auth

callback = Blueprint("callback", __name__)
auth: Auth = current_app.auth

@callback.route("/outh")
def _outh():
    if "token" in session:
        return redirect("/")
    code = request.args.get("code")
    token = auth.access_token(code).access_token
    session["token"] = token
    return redirect("/dashboard")


@callback.route("/login")
def _login():
    if "token" in session:
        return redirect("/dashboard")
    return redirect(current_app.config["AUTH_URL"])

@callback.route("/logout")
def _logout():
    session.clear()
    return redirect("/")

