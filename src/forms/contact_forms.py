from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, FileField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class ContactUsForm(FlaskForm):
    name = StringField("Nombre", validators=[
        DataRequired(),
        Length(min=5, max=100, message="El producto debe contener al menos 5 caracteres.")]
        )
    last_name = StringField("Apellido", validators=[
        DataRequired(),
        Length(min=5, max=100, message="La categoría debe contener al menos 5 caracteres.")]
        )
    email = EmailField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Mensaje", validators=[
        DataRequired(),
        Length(min=20, message="El mensaje debe contener por lo menos 20 caracteres.")]
        )
    submit = SubmitField("Enviar.")
