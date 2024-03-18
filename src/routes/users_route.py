from db_crud.users_crud import user_crud
from flask import Blueprint, request, jsonify, render_template, redirect, flash, g, url_for
from database.db import db
from models import User
from auth.services import get_current_user
from forms import UserUpdateForm 

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/account", methods=["GET", "POST"])
@get_current_user
def my_account():
    form = UserUpdateForm()
    form_in = form.data

    if request.method == "POST" and form.validate_on_submit():
        if not User.query.filter(User.email == form_in["email"] or
                                        User.phone_number == form_in["phone_number"]).first():
            db_user = User.query.filter_by(email=g.user.email).first()
            user_crud.update(obj_in=form_in, db_obj=db_user)
            return redirect(url_for("index"))

        else:
            error = (f"El correo {form.data['email']} o teléfono {form.data['phone_number']} "
                     f"ya se encuentran registrados.")
            flash(error)
    return render_template("users/account/my_account.html", form=form)


@users_blueprint.route("/update")
def update() -> str:
    return "TODO: UPDATE USER"


@users_blueprint.route("/get")
def get() -> str:
    return "TODO: GET USER"


@users_blueprint.route("/get_all")
def get_all() -> str:
    return "TODO: GET ALL USERS"


# print(request.form["asdasd"])
# user_data = request.get_json()  # Se utiliza cuando no se hace uso de algun form para mandar datos
# if not User.query.filter(email = user_data["email"] | phone_number = user_data["phone_number"]).first()
# try:
#     if not User.query.filter(
#         (User.email == user_data["email"]) | (User.phone_number == user_data["phone_number"])
#     ).first():
#         new_user = User(**user_data)
#         db.session.add(new_user)
#         db.session.commit()
#         return new_user.to_json()
#     return jsonify({"message": "El correo o telefono ya se encuentran registrados.",
#                     "status": http_status_message(400)})
# except Exception as e:
#     return f"Error: {str(e)}"
#
# if request.method == "POST":
#     if not models.Product.query.filter_by(name=request.form['name']).first():
#         data = request.form  # Esto entrega un diccionario, utilizarlo al usar forms
#         new_product = models.Product(**data)
#         db.session.add(new_product)
#         db.session.commit()
#         return render_template('index.html')  # Crear url para redireccionar a lista de items
#     error = f"Error: el producto {request.form['name']} ya existe."
#     flash(error)  # esto regresa una lista de mensajes
