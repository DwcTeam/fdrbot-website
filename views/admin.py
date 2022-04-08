from flask import Blueprint, render_template, session, current_app as app, abort
from utlits import is_admin, Auth, convert_data_user
from utlits.checks import only_admin


admin = Blueprint('admin', __name__, url_prefix='/admin')

auth: Auth = app.auth

@admin.route('/')
@only_admin
def index():
    user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
    return render_template('admin.html', user=user, is_admin=True)

@admin.route('/logs')
@only_admin
def logs():
    user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
    return render_template('logs.html', user=user, is_admin=is_admin(user.id))

@index.route('/azkar')
@only_admin
def azkar_page():
    return render_template('azkar.html', title="الصفحة الاذكار")

@index.route('/log-sug')
@only_admin
def log_sug_page():
    return render_template('log-sug.html', title="الصفحة السجلات الاقتراحات")
