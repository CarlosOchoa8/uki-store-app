from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError


class UserCreateForm(FlaskForm):
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
    first_name = StringField("Nombre(s)", validators=[
        DataRequired(),
        Length(min=3, max=50, message="Tu(s) nombre(s) debe(n) tener almenos 3 letras.")]
                             )
    last_name = StringField("Apellido(s)",
                            validators=[DataRequired("Tu(s) apellido(s) debe(n) tener almenos 3 letras."),
                                        Length(min=3, max=50)]
                            )
    email = EmailField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Teléfono", validators=[DataRequired(), Length(max=10, min=10)])
    submit = SubmitField("Actualizar información.")
