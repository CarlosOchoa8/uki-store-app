from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, FileField, SubmitField
from wtforms.validators import DataRequired, Length


class ProductCreateForm(FlaskForm):
    name = StringField("Nombre", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El producto debe contener al menos 5 caracteres.")]
        )
    category = StringField("Categoría", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    price = FloatField("Precio", validators=[DataRequired()])
    main_picture = FileField("Imagen principal", validators=[DataRequired()])
    submit = SubmitField("Añadir producto.")


class ProductUpdateForm(FlaskForm):
    pass