"""Address module forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, FileField, SubmitField
from wtforms.validators import DataRequired, Length


class AddressCreateForm(FlaskForm):
    """Form to create Address model object."""
    first_name = StringField("Nombre", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El producto debe contener al menos 5 caracteres.")]
        )
    last_name = StringField("Nombre", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El producto debe contener al menos 5 caracteres.")]
        )
    company_name = StringField("Categoría", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    address = StringField("Categoría", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    address_detail = StringField("Categoría", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    city = StringField("Categoría", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    country = StringField("País", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    country_region = StringField("Referencia", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La Referencia de la calle debe contener al menos 5 caracteres.")]
        )
    postal_code = StringField("Codigo póstal.", validators=[
        DataRequired(),
        Length(min=5, max=25, message="El código postal debe contener al menos 5 caracteres.")]
        )
    phone_number = StringField("Número de teléfono", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El número telefónico debe contener al menos 5 caracteres.")]
        )

    submit = SubmitField("Añadir producto.")


class AddressUpdateForm(FlaskForm):
    """Form to update Address model object."""
    pass
