from flask import Blueprint, render_template, session, current_app as app
from utlits import is_admin, Auth, convert_data_user
from utlits.checks import only_admin


admin = Blueprint('admin', __name__, url_prefix='/admin')

auth: Auth = app.auth

@admin.route('/')
@only_admin
def index():
    user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
    return render_template('admin.html', user=user, title="لوحة الأدمن")

@admin.route('/logs')
@only_admin
def logs():
    user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
    return render_template('logs.html', user=user, title="سجلات التسجيل بالموقع")

@admin.route('/azkar')
@only_admin
def azkar_page():
    user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
    return render_template('azkar.html', user=user, title="الاذكار")

@admin.route('/suggestions')
@only_admin
def log_sug_page():
    user = convert_data_user(app.logins.find_one({"token.access_token": session["token"]}))
    return render_template('log-sug.html', user=user, title="سجلات الاقتراحات")
