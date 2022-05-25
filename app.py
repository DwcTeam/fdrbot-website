from flask import Flask, g
from flask_cors import CORS
from pymongo import MongoClient
from utlits import Auth
import redis
import views

app = Flask(__name__, instance_relative_config=True)

CORS(app)


app.config.from_pyfile('config.py')
app.secret_key = app.config["SECRET_KEY"]

with app.app_context():
    app.mongodb = MongoClient(app.config["MONGO_URI"]).get_database("fa-azcrone")
    app.col_guilds = app.mongodb.get_collection("guilds")
    app.col_logins = app.mongodb.get_collection("logins")
    app.col_logs = app.mongodb.get_collection("logs")
    app.auth = Auth(app.config['CLIENT_ID'], app.config['CLIENT_SECRET'], app.config['REDIRECT_URI'])
    app.redis = redis.Redis(host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"])


app.register_blueprint(views.guilds)
app.register_blueprint(views.auth)
app.register_blueprint(views.user)
app.register_blueprint(views.index)
app.register_blueprint(views.admin)
app.register_error_handler(404, views.not_found)
app.register_error_handler(403, views.forbidden)

if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="127.0.0.1", port=3939)
    app.run(debug=True, port=4000)

