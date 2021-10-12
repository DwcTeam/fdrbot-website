from flask import Flask
from utlits import Auth


app = Flask(__name__, instance_relative_config=True)
app_ctx = app.app_context()
app_ctx.push()

app.config.from_pyfile("config.py")
app.secret_key = "Dwc Team"

app.auth = Auth(
    client_id=app.config["CLIENT_ID"],
    client_secret=app.config["CLIENT_SECRET"],
    redirect_uri=app.config["REDIRECR_URI"]
)
from views import home, api, dashboard, callback

app.register_blueprint(home)
app.register_blueprint(api)
app.register_blueprint(dashboard)
app.register_blueprint(callback)


if __name__ == "__main__":
    app.run(port="9000", debug=True)
