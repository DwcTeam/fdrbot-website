from flask import Blueprint, render_template, current_app
from utlits import Auth

home = Blueprint('index', __name__)
auth: Auth = current_app.auth

@home.route('/')
def index():
    return render_template("index.html")

@home.route("/bot")
def bot():
    botinfo = auth.bot(current_app.config["TOKEN"])
    return render_template("bot.html", bot=botinfo)

