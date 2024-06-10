"""Users route."""
from flask import (Blueprint, flash, g, redirect, render_template, request,
                   url_for)

from auth.services import get_current_user
from db_crud.users_crud import user_crud
from forms import UserUpdateForm, AddressCreateForm
from models import User

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/mi-cuenta", methods=["GET", "POST"])
@get_current_user
def my_account():
    """User proffile route."""
    form = UserUpdateForm()
    address_form = AddressCreateForm()
    if request.method == "POST" and form.validate_on_submit():
        form_dict = {field: value for field, value in form.data.items() if value not in (None, '', [])}

        if "email" in form_dict and User.query.filter(User.email == form_dict["email"]).first():
            flash(f"El correo {form.data['email']} ya se encuentra registado.")
            return redirect(url_for("users.my_account"))

        if "phone_number" in form_dict and User.query.filter(User.phone_number == form_dict["phone_number"]).first():
            flash(f"El telefono {form.data['phone_number']} ya se encuentra registado.")
            return redirect(url_for("users.my_account"))

        if "email" and "phone_number" not in form_dict:
            db_user = User.query.filter_by(email=g.user.email).first()
            user_crud.update(obj_in=form_dict, db_obj=db_user)
            return redirect(url_for("users.my_account"))

        db_user = User.query.filter(User.email == g.user.email).first()
        user_crud.update(obj_in= form_dict, db_obj= db_user)
        return redirect(url_for("users.my_account"))
    print("VERASDASDS")
    return render_template("users/account/my_account.html", form=form)


@users_blueprint.route("mis-direcciones", methods=["GET", "POST"])
def my_addresses() -> str:
    """Return user logged addresses."""
    form = AddressCreateForm()
    return render_template("users/account/my_addresses.html", address_form=form)


@users_blueprint.route("mis-suscripciones", methods=["GET"])
def my_subcriptions() -> str:
    """Return user logged subcriptions."""
    return render_template("users/account/my_subcriptions.html")


@users_blueprint.route("mi-billetera", methods=["GET"])
def my_wallet() -> str:
    """Return user logged wallet."""
    return render_template("users/account/my_wallet.html")


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
