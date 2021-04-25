from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class CorpTov(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    prize = StringField('Цена', validators=[DataRequired()])
    about = TextAreaField("О нас")
    submit = SubmitField('Далее')
