from smtplib import SMTPException

from flask import (Blueprint, current_app, flash, g, redirect, render_template,
                   request, session, url_for)
from flask_mail import Mail, Message

from forms import ContactUsForm
from models import Product

main_blueprint = Blueprint("ukitukistore", __name__)


@main_blueprint.route("/", methods= ["GET", "POST"])
def index():
    "Return index page"
    products = Product.query.all()
    return render_template("index.html", products=products)


@main_blueprint.route("/sobre-nosotros", methods=["GET"])
def about_us():
    """
    Render template for about us html
    """
    return render_template("about_us.html")


@main_blueprint.route("/faq", methods=["GET"])
def faq():
    """
    Render template for faq html
    """
    return render_template("faq.html")

@main_blueprint.route("/contacto", methods=["GET", "POST"])
def contact_us():
    """
    Render template for faq html
    """
    form = ContactUsForm()
    if request.method == "POST" and form.validate_on_submit():
        form_in = form.data
        name = form_in["name"]
        last_name = form_in["last_name"]
        email = form_in["email"]
        message = form_in["message"]

        mail = Mail(current_app)
        support_mail = Message(subject="Soporte al Cliente - Ukituki Store",
                      recipients=["fidelito6080@gmail.com"])
        support_mail.body = message
        support_mail.html = render_template(
            "support_email.html",
            customer_name=name,
            customer_last_name=last_name,
            customer_email=email,
            customer_message=message
        )

        customer_mail = Message(subject="Soporte al Cliente - Ukituki Store",
                                recipients=[email])
        customer_mail.body = message
        customer_mail.html = render_template(
            "reply_email.html",
            customer_name=name,
            customer_last_name=last_name,
            customer_email=email,
            customer_message=message
        )

        try:
            mail.send(support_mail)
            mail.send(customer_mail)
        except SMTPException as exc:
            flash(
                message=f"Error al enviar el correo: {exc}"
            )
        except Exception as exc:
            flash(
                message=f"Error al enviar el correo: {exc}"
            )
        return redirect(url_for("contact_us"))
    return render_template("contact_us.html", form=form)


main_route = main_blueprint
