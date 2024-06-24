import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, MultipleFileField
from wtforms import (BooleanField, FloatField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from utils.inventory_constants import InventoryStock


class ProductBaseForm(FlaskForm):
    """Base form for a product."""
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
    sku = StringField("SKU", validators=[Optional()])
    product_stock = StringField("Inventario", validators=[DataRequired(message="Stock requerido.")],
                                render_kw={"placeholder": "'Disponible', 'Agotado' o cantidad del producto."},)
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


class ProductCreateForm(ProductBaseForm):
    """Product Create form."""


class ProductUpdateForm(ProductBaseForm):
    """Product Update form."""
    name = StringField("Nombre", validators=[
        Optional(),
        Length(min=5, max=100, message="El producto debe contener al menos 5 caracteres.")]
        )
    category = StringField("Categoría", validators=[
        Optional(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    price = FloatField("Precio", validators=[Optional()])
    label = StringField("Etiqueta", validators=[Optional()])
    description = TextAreaField("Descripción", validators=[Optional()])
    sku = StringField("SKU", validators=[Optional()])
    product_stock = StringField("Inventario", validators=[Optional()],
                                render_kw={"placeholder": "'Disponible', 'Agotado' o cantidad del producto."},)
    main_picture = MultipleFileField("Imagen principal",
                                     validators=[Optional(), FileAllowed(["jpg", "png", "jpeg"])])
    available = BooleanField("Mostrar producto en tienda.", validators=[Optional()])
    submit = SubmitField("Añadir producto.")
