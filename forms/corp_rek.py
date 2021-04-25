from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class CorpRek(FlaskForm):
    prize = StringField('Цена', validators=[DataRequired()])
    # viewers_age = StringField('Зрители', validators=[DataRequired()])
    about = TextAreaField("О нас")
    submit = SubmitField('Зарегистрироваться')

    # email = EmailField('Почта', validators=[DataRequired()])
    # password = PasswordField('Пароль', validators=[DataRequired()])
    # password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    # name = StringField('Имя пользователя', validators=[DataRequired()])
    # submit = SubmitField('Далее')
