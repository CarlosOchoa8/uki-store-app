from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, MultipleFileField
from wtforms import FloatField, MultipleFileField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ProductCreateForm(FlaskForm):
    """Product create form."""
    name = StringField("Nombre", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El producto debe contener al menos 5 caracteres.")]
        )
    category = StringField("Categoría", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    price = FloatField("Precio", validators=[DataRequired()])
    # main_picture = FileField("Imagen principal", validators=[DataRequired()])
    main_picture = MultipleFileField("Imagen principal",
                                     validators=[
                                         DataRequired(),
                                         FileAllowed(["jpg", "png", "jpeg"])
                                         ])
    submit = SubmitField("Añadir producto.")


class ProductUpdateForm(FlaskForm):
    """pass """
    pass