from flask import Blueprint, render_template, redirect, current_app
from utlits import get_channels_count, get_guilds_count, get_users_count, get_shards_count

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
    channels_count = get_channels_count()
    guilds_count = get_guilds_count()
    users_count = get_users_count()
    shards_count = get_shards_count()
    return render_template('index.html', channels_count=channels_count, guilds_count=guilds_count, users_count=users_count, shards_count=shards_count)

@index.route('/invite')
def invite_page():
    return redirect(f"https://discord.com/api/oauth2/authorize?client_id={current_app.config['CLIENT_ID']}&permissions=8&scope=bot%20applications.commands")

@index.route("/commands")
def commands_page():
    return render_template('commands.html')
