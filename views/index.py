import json
from flask import Blueprint, jsonify, current_app as app


index = Blueprint('index', __name__)

@index.route('/')
def index_route():
    return jsonify({"status": "ok"})

@index.route("/stats")
def stats():
    with app.app_context():
        redis = app.redis
    return jsonify(json.loads(redis.get("bot:stats")))
