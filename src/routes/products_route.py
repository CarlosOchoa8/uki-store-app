from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash, Response
)

from db_crud import product_crud
from models import Product  # con esto se migran a la base de datos
from auth.services import get_current_user
from forms import ProductCreateForm

products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/create", methods=['GET', "POST"])
@get_current_user
def create() -> Response | str:
    form = ProductCreateForm()
    form_in = form.data
    if request.method == "POST" and form.validate_on_submit():
        if not Product.query.filter_by(name=form_in["name"]).first():
            product_crud.create(obj_in=form_in)
            return redirect(url_for("index"))  # Crear url para redireccionar a lista de items
        error = f"Error: el producto {request.form['name']} ya existe."
        flash(error)  # esto regresa una lista de mensajes
    return render_template('products/add_product.html', form=form)


@products_blueprint.route("/update")
def update() -> str:
    return "TODO: UPDATE PRODUCT"


@products_blueprint.route("/get")
def get() -> str:
    return "TODO: GET PRODUCT"


@products_blueprint.route("/get_all", methods=["GET"])
def get_all() -> Response:
    """Returns: The rendered template with the products to display."""
    page = request.args.get("page", 1,  type=int)
    products = product_crud.get_multi(page=page)
    print(type(render_template("products/store.html", products=products)))
    return render_template("products/store.html", products=products)
