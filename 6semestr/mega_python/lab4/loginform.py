from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, EmailField
#import wtforms
from wtforms import FileField, RadioField
from wtforms.validators import DataRequired, Email
import json
import email_validator

#wtforms.SelectMultipleField

prof = ["инженер-исследователь", "пилот, строитель",
"экзобиолог", "врач", "инженер по терраформированию", "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", 
"инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер",
"штурман", "пилот дронов"]

class LoginForm(FlaskForm):
    last_name = StringField('Имя', validators=[DataRequired()])
    first_name = StringField('Фамилия', validators=[DataRequired()])
    email = EmailField('email', validators=[Email()])
    education = StringField('образование', validators=[DataRequired()])
    profecion = SelectField('профессия', choices=prof)
    sex = RadioField('Пол', choices = [('M','Мужской'),('F','Женский')])
    motivation = StringField('Мотивация', validators=[DataRequired()])
    ready = BooleanField('Готовы остаться на Марсе?')
    photo = FileField('Фотография')
    submit = SubmitField('Отправить')

