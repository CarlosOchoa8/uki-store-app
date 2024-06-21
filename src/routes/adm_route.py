from flask import Blueprint, Response, render_template, request

from forms import ProductCreateForm

panel_blueprint = Blueprint("panel", __name__)


@panel_blueprint.route("/", methods=['GET', "POST"])
def panel() -> Response | str:
    """Render admin panel."""
    return render_template("adm_base.html")


@panel_blueprint.route("/product/create", methods=["GET", "POST"])
def create_product():
    """Add new product at store."""
    print("Entro")
    form = ProductCreateForm()
    if request.method == "POST" and form.validate_on_submit():
        print("asdasd")
    return render_template("adm/products/create.html", form=form)


panel_route = panel_blueprint
