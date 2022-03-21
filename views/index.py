from flask import Blueprint, render_template, redirect, current_app, session
from utlits import get_bot_info, get_commands

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
    bot = get_bot_info()
    return render_template(
        'index.html', is_login=True if "token" in session else False, 
        channels_count=bot["channels"], shards_count=bot["shards"], 
        commands_count=len(get_commands()), guilds_count=bot["guilds"],
        title="الصفحة الرئيسية"
    )

@index.route('/invite')
def invite_page():
    return redirect(f"https://discord.com/api/oauth2/authorize?client_id={current_app.config['CLIENT_ID']}&permissions=8&scope=bot%20applications.commands")

@index.route('/support')
def support_page():
    return redirect("https://discord.com/invite/EpZJwpSgka")

@index.route("/commands")
def commands_page():
    return render_template(
        'commands.html', commands=get_commands(), 
        is_login=True if "token" in session else False,
        title="الأوامر"
    )

@index.route("/about")
def about_page():
    return render_template(
        "about.html", is_login=True if "token" in session else False,
        title="عن البوت"
    )
