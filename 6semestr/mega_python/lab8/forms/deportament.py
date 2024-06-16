from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired
prof = ["инженер-исследователь", "пилот, строитель",
"экзобиолог", "врач", "инженер по терраформированию", "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", 
"инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер",
"штурман", "пилот дронов"]

class DeportamentForm(FlaskForm):
    title = StringField('Название депортамента', validators=[DataRequired()])
    chief = SelectField('Начальник депортамента', validators=[DataRequired()])
    members = SelectMultipleField('Участники', validators=[DataRequired()], validate_choice=False)
    email = EmailField('Почта', validators=[DataRequired()])
    submit = SubmitField('Добавить')