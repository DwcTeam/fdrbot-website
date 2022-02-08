from flask import Blueprint, render_template, current_app, session
from utlits import login_required, Auth

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

auth = Auth(current_app.config['CLIENT_ID'], current_app.config['CLIENT_SECRET'], current_app.config['REDIRECT_URL'])

@dashboard.route('/')
@login_required
def index_page():
    guilds = auth.user(session['token']).guilds()
    available_guilds = [i for i in guilds]
    unavailable_guilds = [i for i in guilds]
    return render_template('dashboard.html', available_guilds=available_guilds, unavailable_guilds=unavailable_guilds)

@dashboard.route('/<int:guild_id>')
@login_required
def guild_page(guild_id):
    guild = auth.user(session['token']).get_guild(guild_id)
    if isinstance(guild, dict):
        return "يا بزر مالك صلاحيات"
    return render_template('guild.html', guild=guild)

