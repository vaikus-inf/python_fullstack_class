from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email

class AuthForm(FlaskForm):
    name = StringField('Имя: ', validators=[DataRequired()])
    email = EmailField('Почта: ', validators=[DataRequired()])
    passoword = PasswordField('Пароль: ', validators=[DataRequired()])
    submit = SubmitField('Отправить')