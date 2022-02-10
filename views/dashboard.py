from flask import Blueprint, render_template, current_app, session
from utlits import login_required, Auth, check_guild, guild_info, get_guild_channels, get_guild_roles

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

auth = Auth(current_app.config['CLIENT_ID'], current_app.config['CLIENT_SECRET'], current_app.config['REDIRECT_URI'])

@dashboard.route('/')
@login_required
def index_page():
    guilds = auth.user(session['token']).guilds()
    available_guilds = [i for i in guilds if check_guild(i.id)]
    unavailable_guilds = [i for i in guilds if i not in available_guilds]
    return render_template('dashboard.html', available_guilds=available_guilds, unavailable_guilds=unavailable_guilds)

@dashboard.route('/<int:guild_id>')
@login_required
def guild_page(guild_id):
    guild = auth.user(session['token']).get_guild(guild_id)
    if isinstance(guild, dict):
        return "يا بزر مالك صلاحيات"
    info = guild_info(guild_id)
    channels = get_guild_channels(guild_id)
    text_channels = [i for i in channels if i.type == 0]
    voice_channels = [i for i in channels if i.type == 2]
    roles = get_guild_roles(guild_id)
    return render_template('guild.html', guild=guild, info=info, text_channels=text_channels, voice_channels=voice_channels, roles=roles)

