"""Auth module for login and logout features"""
from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from sqlalchemy import or_

# from werkzeug.security import check_password_hash
from auth.jwt_settings import bcrypt
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
        flash(f"El correo o teléfono ya se encuentran registrados.")
    return render_template('users/auth/sign_up.html', form=form)


@auth_blueprint.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        user_data = request.form
        error = None
        # TODO: verificar que no entre al regresar None
        if user := User.query.filter_by(email=user_data["email"]).first():
            if not bcrypt.check_password_hash(user.password, user_data["password"]):
                error = "Los datos son incorrectos."

            # Inicio de sesion
            if not error:
                session.clear()  # limpiar sesion iniciada
                session["user_id"] = user.id  # Se inicia sesion
                return redirect(url_for("index"))

        flash(error)
    return render_template('users/auth/sign_in.html')


@auth_blueprint.route("/log_out")
def logout():
    session.clear()
    return redirect(url_for("index"))


@auth_blueprint.before_app_request  # Se registra a manera de dependencia para que se ejecute antes de cada petición
def load_logged_user():
    user_id = session.get("user_id")  # obtener id del usuario logeado
    if user_id is None:
        g.user = None
    # si existe usuario logeado, se obtiene de la db.
    # Se mantiene la sesion
    else:
        g.user = User.query.get_or_404(user_id)
