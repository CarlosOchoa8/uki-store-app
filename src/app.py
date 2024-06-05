"""Init for Flask app module."""
from smtplib import SMTPException
from typing import Any

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mail import Mail, Message

import models
from config2 import config
from database.db import db
from forms.contact_forms import ContactUsForm
from routes import (address_blueprint, auth_blueprint, main_blueprint,
                    products_blueprint, users_blueprint)

app = Flask(__name__)
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

app_config = config.AppConfig()
app.config.from_object(app_config)
db.init_app(app)

app.register_blueprint(auth_blueprint, url_prefix="/app/v1/auth")
app.register_blueprint(users_blueprint, url_prefix="/app/v1/users")
app.register_blueprint(products_blueprint, url_prefix="/app/v1/products")
app.register_blueprint(main_blueprint, url_prefix="/ukitukistore")

with app.app_context():
    # db.drop_all()
    db.create_all()

@app.route("/")
def index():
    return "{'message': 'OK'}"
    # print(app.blueprints)
    # products = models.Product.query.all()
    # return render_template("index.html", products=products)


# @app.route("/about_us", methods=["GET"])
# def about_us():
#     """
#     Render template for about us html
#     """
#     return render_template("about_us.html")


# @app.route("/faq", methods=["GET"])
# def frecuent_questions_answers():
#     """
#     Render template for faq html
#     """
#     return render_template("faq.html")

# @app.route("/contact_us", methods=["GET", "POST"])
# def contact_us():
#     """
#     Render template for faq html
#     """
#     form = ContactUsForm()
#     if request.method == "POST" and form.validate_on_submit():
#         # TODO
#         form_in = form.data
#         name = form_in["name"]
#         last_name = form_in["last_name"]
#         email = form_in["email"]
#         message = form_in["message"]

#         mail = Mail(app)
#         support_mail = Message(subject="Soporte al Cliente - Ukituki Store",
#                       recipients=["fidelito6080@gmail.com"])
#         support_mail.body = message
#         support_mail.html = render_template(
#             "support_email.html",
#             customer_name=name,
#             customer_last_name=last_name,
#             customer_email=email,
#             customer_message=message
#         )

#         customer_mail = Message(subject="Soporte al Cliente - Ukituki Store",
#                                 recipients=[email])
#         customer_mail.body = message
#         customer_mail.html = render_template(
#             "reply_email.html",
#             customer_name=name,
#             customer_last_name=last_name,
#             customer_email=email,
#             customer_message=message
#         )

#         try:
#             mail.send(support_mail)
#             mail.send(customer_mail)
#         except SMTPException as exc:
#             flash(
#                 message=f"Error al enviar el correo: {exc}"
#             )
#         except Exception as exc:
#             flash(
#                 message=f"Error al enviar el correo: {exc}"
#             )
#         return redirect(url_for("contact_us"))
#     return render_template("contact_us.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
