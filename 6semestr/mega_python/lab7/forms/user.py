from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, SelectField, BooleanField
from wtforms.validators import DataRequired

prof = [
    "инженер-исследователь", "пилот, строитель", "экзобиолог", "врач",
    "инженер по терраформированию", "климатолог",
    "специалист по радиационной защите", "астрогеолог", "гляциолог",
    "инженер жизнеобеспечения", "метеоролог", "оператор марсохода",
    "киберинженер", "штурман", "пилот дронов"
]


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = StringField('Возраст', validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = SelectField('Профессия',
                             validators=[DataRequired()],
                             choices=prof)
    addres = StringField('Адрес модуля', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль',
                                   validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')