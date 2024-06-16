from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = SelectField('Ответсвенный',
                              validators=[DataRequired()],
                              validate_choice=False)
    job = TextAreaField('Описание работы', validators=[DataRequired()])
    work_size = StringField('Время работы в часах',
                            validators=[DataRequired()])
    collaborators = SelectMultipleField('Участники',
                                        validators=[DataRequired()],
                                        validate_choice=False)
    categori = SelectMultipleField("Категории",validate_choice=False)
    is_finished = BooleanField("Завершена?")
    submit = SubmitField('Добавить')
