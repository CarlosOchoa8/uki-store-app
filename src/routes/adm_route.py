from flask import Blueprint, Response, render_template

panel_blueprint = Blueprint("panel", __name__)


@panel_blueprint.route("/", methods=['GET', "POST"])
def panel() -> Response | str:
    """Render admin panel."""
    return render_template("adm_base.html")


panel_route = panel_blueprint
