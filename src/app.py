"""Init for Flask app module."""
from typing import Any

from flask import Flask, jsonify, render_template

from auth.jwt_settings import bcrypt, jwt
from config2 import config
from database.db import db
from routes import (auth_blueprint, main_blueprint, panel_route,
                    products_blueprint, users_blueprint)

app = Flask(__name__)
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

class PrefixMiddleware:
    """Middleware for url path name"""
    def __init__(self, app, prefix) -> None:
        self.app = app
        self.prefix = prefix


    def __call__(self, environ, start_response) -> Any:
        if environ["PATH_INFO"].startswith(self.prefix):
            environ["PATH_INFO"] = environ["PATH_INFO"][len(self.prefix):]
            environ["SCRIPT_NAME"] = self.prefix
        elif environ["PATH_INFO"] == "/":
            environ["PATH_INFO"] = "/index.html"
        return self.app(environ, start_response)

app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix="/ukitukistore")

# TODO ordenar todo esto
app_config = config.AppConfig()
app.config.from_object(app_config)
db.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth_blueprint, url_prefix="/app/v1/auth")
app.register_blueprint(users_blueprint, url_prefix="/app/v1/users")
app.register_blueprint(products_blueprint, url_prefix="/app/v1/products")
app.register_blueprint(main_blueprint, url_prefix="/ukitukistore")
app.register_blueprint(panel_route, url_prefix="/panel")

with app.app_context():
    # db.drop_all()
    db.create_all()

@app.route("/")
def index():
    """Root method to check app availability."""
    return jsonify({"Service": "Ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
