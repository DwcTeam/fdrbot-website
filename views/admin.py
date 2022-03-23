from flask import Blueprint, render_template, session, current_app as app, url_for, abort
from utlits import is_admin, AccessToken, Auth


admin = Blueprint('admin', __name__, url_prefix='/admin')

auth = Auth(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'], app.config['REDIRECT_URI'])

@admin.route('/')
def index():
    user = auth.user(AccessToken(**app.logins.find_one({"token.access_token": session["token"]}).get("token")))
    if not is_admin(user.id):
        return abort(403)
    return render_template('admin.html', user=user, is_admin=True)

@admin.route('/logs')
def logs():
    user = auth.user(AccessToken(**app.logins.find_one({"token.access_token": session["token"]}).get("token")))
    if not is_admin(user.id):
        return abort(403)
    return render_template('logs.html', user=user, is_admin=is_admin(user.id))
