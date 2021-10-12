from flask import Blueprint, session, redirect, render_template, current_app
from utlits import login_required, Auth


dashboard = Blueprint("dashboard", __name__)
auth: Auth = current_app.auth

@dashboard.route("/dashboard/<guild_id>", methods=["GET"])
@login_required
def _dashboard(guild_id):
    return "OKS"

@dashboard.route("/dashboard", methods=["GET"])
@login_required
def _dashboard_guild():
    token = session.get("token")
    guilds = auth.user(token).guilds()
    return render_template("dashboard.html", guilds=guilds)

