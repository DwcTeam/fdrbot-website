from flask import Flask, render_template
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__, instance_relative_config=True)

CORS(app)

app_ctx = app.app_context()
app_ctx.push()

app.config.from_pyfile('config.py')
app.secret_key = app.config["SECRET_KEY"]
app.mongodb = MongoClient(app.config["MONGO_URI"]).get_database("fa-azcrone")
app.db = app.mongodb.get_collection("guilds")
app.logins = app.mongodb.get_collection("logins")

import views

app.register_blueprint(views.api)
app.register_blueprint(views.auth)
app.register_blueprint(views.dashboard)
app.register_blueprint(views.index)
app.register_blueprint(views.admin)
app.register_error_handler(404, views.not_found)
app.register_error_handler(403, views.forbidden)

if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="127.0.0.1", port=3939)
    app.run(debug=True, port=3939)

