from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional


class UserCreateForm(FlaskForm):
    """Form for request data for User creation"""
    first_name = StringField("Nombre(s)", validators=[
        DataRequired(),
        Length(min=3, max=50, message="Tu(s) nombre(s) debe(n) tener almenos 3 letras.")]
                             )
    last_name = StringField("Apellido(s)",
                            validators=[DataRequired("Tu(s) apellido(s) debe(n) tener almenos 3 letras."),
                                        Length(min=3, max=50)]
                            )
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6, max=50)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Teléfono", validators=[])
    submit = SubmitField("Registrar.")


class UserUpdateForm(FlaskForm):
    """Form for request data for User Updating"""
    first_name = StringField("Nombre(s)",
                             validators=[
                                 Optional(""),
                                 Length(min=3, max=50, message="Tu(s) nombre(s) debe(n) tener almenos 3 letras.")]
                                 )
    last_name = StringField("Apellido(s)",
                            validators=[Optional(),
                                        Length(min= 3,
                                               max= 50,
                                               message= "Tu(s) nombre(s) debe(n) tener almenos 3 letras.")],
                                               )
    email = EmailField("Email", validators=[Optional(),
                                            Email(message="Dirección email inválida.")])
    phone_number = StringField("Teléfono", validators=[Optional(),
                                                       Length(
                                                           max=10,
                                                           min=10,
                                                           message="El número debe contener 10 dígitos.")]
                                                           )
    submit = SubmitField("Actualizar información.")
