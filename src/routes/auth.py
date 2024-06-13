"""Auth module for login and logout features"""
from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from sqlalchemy import or_

from auth.services import generate_token
from db_crud import user_crud
from forms import UserCreateForm
from models import User

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = UserCreateForm()
    form_in = form.data

    if request.method == "POST" and form.validate_on_submit():
        if not User.query.filter(or_(User.email == form_in["email"],
                                        User.phone_number == form_in["phone_number"])).first():
            user_crud.create(obj_in=form_in)
            return redirect(url_for("index"))
        flash("El correo o teléfono ya se encuentran registrados.")
    return render_template('users/auth/sign_up.html', form=form)


@auth_blueprint.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        user_data = request.form
        # TODO: verificar que no entre al regresar None
        try:
            token, user = generate_token(user_data)
            token_json = token.get_json()

            # Inicio de sesion
            session.clear()
            session["user_id"] = user.id  # Se inicia sesion
            redirect_response = redirect(url_for("ukitukistore.index"))
            redirect_response.set_cookie(
                "access_token",
                token_json["access_token"],
                httponly=True,
                secure=True,
                samesite='Strict'
                )
            return redirect_response
        except Exception as exc:
            flash(exc)
    return render_template('users/auth/sign_in.html')


@auth_blueprint.route("/log_out")
def logout():
    """Clear user session and cookies."""
    session.clear()
    logout_response = redirect(url_for("ukitukistore.index"))
    logout_response.set_cookie("access_token", "", expires=0)
    return logout_response


@auth_blueprint.before_app_request  # Se registra a manera de dependencia para que se ejecute antes de cada petición
def load_logged_user():
    """Load user logged in session."""
    user_id = session.get("user_id")  # obtener id del usuario logeado
    if user_id is None:
        g.user = None
    # si existe usuario logeado, se obtiene de la db.
    # Se mantiene la sesion
    else:
        g.user = User.query.get_or_404(user_id)
