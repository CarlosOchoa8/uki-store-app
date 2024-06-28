from flask import (Blueprint, Response, redirect, render_template, request,
                   url_for, flash)
from db_crud import product_crud, inventory_crud
from forms import ProductCreateForm, ProductUpdateForm
from models import Product, Inventory

panel_blueprint = Blueprint("panel", __name__)


@panel_blueprint.route("/", methods=['GET', "POST"])
def panel() -> Response | str:
    """Render admin panel."""
    return render_template("adm_base.html")

# TODO validar que el usuario sea admin y este logeado
@panel_blueprint.route("/product/create", methods=["GET", "POST"])
def create_product():
    """Add new product at store."""
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


# TODO validar que el usuario sea admin y este logeado
@panel_blueprint.route("/inventory", methods=["GET", "POST"])
def inventory():
    """Inventory of products."""
    prod_inventory = inventory_crud.get_multi()
    return render_template("adm/products/inventory.html", inventory=prod_inventory)


# TODO validar que el usuario sea admin y este logeado
@panel_blueprint.route("/productos", methods=["GET", "POST"])
def get_products():
    """Get all products."""
    products = product_crud.get_products_data()
    return render_template("adm/products/products.html", products=products)


# TODO validar que el usuario sea admin y este logeado
@panel_blueprint.route("/product/<int:product_id>", methods=["GET", "POST"])
def update_product(product_id: int):
    """Update a product."""
    product_form = ProductUpdateForm()
    product = product_crud.get(id=product_id)

    if request.method == "POST" and product_form.validate_on_submit():
        product_in = product_form.data
        if product_crud.get_by_name(name=product_in["name"]) or product_crud.get_by_sku(sku=product_in["sku"]):
            error = "Error: el nombre o sku ya se encuentra registrado."
            flash(error)
        product_crud.update(obj_in=product_in, db_obj=product)
        redirect(url_for('panel.update_product', product_id=product.id), 200)

    return render_template("adm/products/update.html", form=product_form, product=product)


panel_route = panel_blueprint
