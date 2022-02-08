from flask import Blueprint, redirect, request, session, current_app, after_this_request
from utlits import login_required, Auth

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return redirect(current_app.config['REDIRECT_URL'])

@auth.route('/outh')
def outh():
    if "token" in session:
        return redirect("/dashboard")
    auth = Auth(current_app.config['CLIENT_ID'], current_app.config['CLIENT_SECRET'], current_app.config['REDIRECT_URL'])
    access_token = auth.access_token(request.args.get('code'))
    session['token'] = access_token.access_token
    print(session.values())
    return redirect("/dashboard")


@auth.route('/logout')
def logout():
    session.clear()
    return redirect("/")
