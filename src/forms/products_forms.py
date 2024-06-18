import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, MultipleFileField
from wtforms import FloatField, StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from utils.inventory_constants import InventoryStock


class ProductCreateForm(FlaskForm):
    """Product create form."""
    name = StringField("Nombre", validators=[
        DataRequired(message="Nombre requerido"),
        Length(min=5, max=100, message="El producto debe contener al menos 5 caracteres.")]
        )
    category = StringField("Categoría", validators=[
        DataRequired("Categoría requerida."),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    price = FloatField("Precio", validators=[DataRequired(message="Precio requerido.")])
    label = StringField("Etiqueta")
    description = TextAreaField("Descripción")
    # main_picture = FileField("Imagen principal", validators=[DataRequired()])
    sku = StringField("SKU", validators=[Optional()])
    product_stock = StringField("Inventario", validators=[])
    main_picture = MultipleFileField("Imagen principal",
                                     validators=[
                                         DataRequired(message="Foto referencial de producto."),
                                         FileAllowed(["jpg", "png", "jpeg"])
                                         ])
    available = BooleanField("Mostrar producto en tienda.")
    submit = SubmitField("Añadir producto.")

    def validate_product_stock(form, field):
        if field.data not in [InventoryStock.UNAVAILABLE.value,
                              InventoryStock.AVAILABLE.value] and not re.match(r"^\d+$", field.data):
            raise ValidationError("""Debes proporcionar stock de inventario o cantidad válida
                                  ('Disponible', 'Agotado' o Cantidad).""")


class ProductUpdateForm(FlaskForm):
    """pass """
    pass
