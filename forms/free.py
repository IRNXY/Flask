from flask_wtf import FlaskForm
from wtforms import  SubmitField


class Free(FlaskForm):
    submit = SubmitField('Далее')
