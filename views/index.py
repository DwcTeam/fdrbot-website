from flask import Blueprint, jsonify, render_template, redirect, current_app, session
from utlits import get_bot_info, get_commands

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
    return jsonify({"status": "ok"})

@index.route("/stats")
def stats():
    return jsonify(get_bot_info())

@index.route('/suggestions')
def suggestions_page():
    return render_template('suggestions.html', title="الصفحة الاقتراحات")


@index.route('/invite')
def invite_page():
    return redirect(f"https://discord.com/api/oauth2/authorize?client_id={current_app.config['CLIENT_ID']}&permissions=8&scope=bot%20applications.commands")

@index.route('/vote')
def vote_page():
    return redirect(f"https://top.gg/bot/{current_app.config['CLIENT_ID']}/vote")


@index.route('/support')
def support_page():
    return redirect("https://discord.com/invite/EpZJwpSgka")

@index.route("/commands")
def commands_page():
    return render_template(
        'commands.html', commands=get_commands(), 
        title="الأوامر"
    )

@index.route("/about")
def about_page():
    return render_template(
        "about.html",
        title="عن البوت"
    )
