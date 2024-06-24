from flask_wtf import FlaskForm
from wtforms import (EmailField, FileField, FloatField, PasswordField,
                     StringField, SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Email, Length


class InventoryCreateForm(FlaskForm):
    """Create object in inventory"""
    pass


class InventoryUpdateForm(FlaskForm):
    """Update object in inventory"""
    pass