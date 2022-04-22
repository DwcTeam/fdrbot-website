from flask import Blueprint, jsonify
from utlits import get_bot_info

index = Blueprint('index', __name__)

@index.route('/')
def index_route():
    return jsonify({"status": "ok"})

@index.route("/stats")
def stats():
    return jsonify(get_bot_info())
