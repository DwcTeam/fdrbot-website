from flask import Blueprint, jsonify, render_template, redirect, current_app, session
from utlits import get_bot_info, get_commands

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
    return jsonify({"status": "ok"})

@index.route("/stats")
def stats():
    return jsonify(get_bot_info())


@index.route("/commands")
def commands():
    return jsonify(get_commands())
