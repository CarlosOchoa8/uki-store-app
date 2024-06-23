from flask import (Blueprint, Response, redirect, render_template, request,
                   url_for, flash)
from db_crud import product_crud
from forms import ProductCreateForm
from models import Product

panel_blueprint = Blueprint("panel", __name__)


@panel_blueprint.route("/", methods=['GET', "POST"])
def panel() -> Response | str:
    """Render admin panel."""
    return render_template("adm_base.html")

# TODO validar que el usuario sea admin y este logeado
@panel_blueprint.route("/product/create", methods=["GET", "POST"])
def create_product():
    """Add new product at store."""
    print("Entro")
    form = ProductCreateForm()
    form_in = form.data
    if request.method == "POST" and form.validate_on_submit():
        if not Product.query.filter_by(name=form_in["name"]).first():
            product_crud.create(obj_in=form_in)
            flash("Producto creado exitosamente.", "success")
            return redirect(url_for("panel.create_product"))
        error = f"Error: el producto {request.form['name']} ya existe."
        flash(error)  # esto regresa una lista de mensajes
    return render_template("adm/products/create.html", form=form)


panel_route = panel_blueprint
