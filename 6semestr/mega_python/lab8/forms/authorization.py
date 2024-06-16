from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, SelectField, BooleanField
from wtforms.validators import DataRequired


class AuthorizationForm(FlaskForm):
    enter = SubmitField('Войти')
    registracion = SubmitField('Зарегестрироваться')