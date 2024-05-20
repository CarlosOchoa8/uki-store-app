"""Init for Flask app module."""
from flask import Flask, render_template

from database.db import db
from routes import (
    auth_blueprint,
    users_blueprint,
    products_blueprint
)
import models
from config2 import config

app = Flask(__name__)
app_config = config.Config()
app.config.from_object(app_config)
db.init_app(app)

app.register_blueprint(auth_blueprint, url_prefix="/app/v1/auth")
app.register_blueprint(users_blueprint, url_prefix="/app/v1/users")
app.register_blueprint(products_blueprint, url_prefix="/app/v1/products")

with app.app_context():
    # db.drop_all()
    db.create_all()

@app.route("/")
def index():
    # TODO: Determinar donde y como colocar esta ruta
    products = models.Product.query.all()
    return render_template("index.html", products=products)


@app.route("/about_us", methods=["GET"])
def about_us():
    """
    Render template for about us html
    """
    return render_template("about_us.html")


@app.route("/faq", methods=["GET"])
def frecuent_questions_answers():
    """
    Render template for faq html
    """
    return render_template("faq.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
