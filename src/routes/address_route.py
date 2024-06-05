from flask import (Blueprint, Response, flash, redirect, render_template,
                   request, url_for)

from auth.services import get_current_user
from db_crud import address_crud
from forms import ProductCreateForm
from models import Address

address_blueprint = Blueprint("address", __name__)


@address_blueprint.route("/mis-direcciones", methods=['GET', "POST"])
def my_addresses() -> Response | str:
    return "MIS DIRECCIONES URL"


@address_blueprint.route("/update")
def update() -> str:
    return "TODO: UPDATE PRODUCT"


@address_blueprint.route("/get")
def get() -> str:
    return "TODO: GET PRODUCT"


@address_blueprint.route("/get_all/", methods=["GET"])
def get_all() -> Response:
    """Returns: The rendered template with the products to display."""
    pass
