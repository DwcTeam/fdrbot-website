from flask import Blueprint, render_template, redirect, current_app

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
    return render_template('index.html')

@index.route('/invite')
def invite_page():
    return redirect(f"https://discord.com/api/oauth2/authorize?client_id={current_app.config['CLIENT_ID']}&permissions=8&scope=bot%20applications.commands")

@index.route("/commands")
def commands_page():
    return render_template('commands.html')
