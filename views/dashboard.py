from flask import Blueprint, render_template, current_app as app, session, abort
from utlits import (
    login_required, Auth, get_guild, check_permission, AccessToken, check_guild
)

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

auth = Auth(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'], app.config['REDIRECT_URI'])

@dashboard.route('/')
@login_required
def index_page():
    user = auth.user(AccessToken(**app.logins.find_one({"token.access_token": session["token"]}).get("token")))
    guilds = user.guilds()
    available_guilds = [i for i in guilds if check_guild(i.id)]
    unavailable_guilds = [i for i in guilds if i not in available_guilds]
    return render_template(
        'dashboard.html', available_guilds=available_guilds, unavailable_guilds=unavailable_guilds,
        title="لوحة التحكم", user=user
    )

@dashboard.route('/<int:guild_id>')
@login_required
def guild_page(guild_id):
    user = auth.user(AccessToken(**app.logins.find_one({"token.access_token": session["token"]}).get("token")))
    user_guild = user.get_guild(guild_id)
    # if guild is missing
    if not user_guild :
        return abort(403)
    # get guild info form database
    info = app.db.find_one({"_id": guild_id})
    if not info:
        info = {
            "_id": guild_id,
            "prefix": "!",
            "channel": None,
            "time": 1800,
            "anti_spam": False,
            "embed": False,
            "role_id": None
        }
        app.db.insert_one(info)
    guild = get_guild(guild_id)
    text_channels = [i for i in guild.channels if i.type == 0]
    voice_channels = [i for i in guild.channels if i.type == 2]
    return render_template(
        'guild.html', guild=user_guild, info=info, text_channels=text_channels, 
        voice_channels=voice_channels, roles=guild.roles,
        title=f"{user_guild.name} | لوحة التحكم"
    )

