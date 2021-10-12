from flask import Blueprint, session, redirect
from utlits import login_required

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard/<guild_id>", methods=["GET"])
@login_required
def _dashboard(guild_id):
    return "OKS"

@dashboard.route("/dashboard", methods=["GET"])
@login_required
def _dashboard_guild():
    return "WOW"

