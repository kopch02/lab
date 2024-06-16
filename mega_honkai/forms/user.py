from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, SelectField, BooleanField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Ваше имя:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    password_re = PasswordField('Повторите пароль:', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')