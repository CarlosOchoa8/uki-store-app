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
    last_name = StringField("Apellido", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El producto debe contener al menos 5 caracteres.")]
        )
    company_name = StringField("Nombre de la empresa", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El nombre de la empresa debe contener al menos 5 caracteres.")]
        )
    address = StringField("Dirección", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La dirección debe contener al menos 5 caracteres.")]
        )
    address_detail = StringField("Dirección - Línea 2", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La referencia debe contener al menos 5 caracteres.")]
        )
    city = StringField("Ciudad", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La ciudad debe contener al menos 5 caracteres.")]
        )
    country = StringField("País", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El pais debe contener al menos 5 caracteres.")]
        )
    country_region = StringField("Región", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La región de la calle debe contener al menos 5 caracteres.")]
        )
    postal_code = StringField("Código póstal.", validators=[
        DataRequired(),
        Length(min=5, max=25, message="El código postal debe contener al menos 5 caracteres.")]
        )
    phone_number = StringField("Teléfono", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El número telefónico debe contener al menos 5 caracteres.")]
        )

    submit = SubmitField("Añadir producto.")


class AddressUpdateForm(FlaskForm):
    """Form to update Address model object."""
    pass
