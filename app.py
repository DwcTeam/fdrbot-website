from flask import Flask
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)

CORS(app)

app_ctx = app.app_context()
app_ctx.push()

app.config.from_pyfile('config.py')
app.secret_key = app.config["SECRET_KEY"]

import views

app.register_blueprint(views.api)
app.register_blueprint(views.auth)
app.register_blueprint(views.dashboard)
app.register_blueprint(views.index)
app.register_blueprint(views.errors)

if __name__ == '__main__':
    app.run(debug=True, port=3939)

