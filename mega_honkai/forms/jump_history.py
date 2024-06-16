from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class Jump_History_Form(FlaskForm):
    url_history = StringField("ссылка:", validators=[DataRequired()])
    submit = SubmitField('Импортировать')