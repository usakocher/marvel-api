from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import UserMixin


class UserSignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    confirm = PasswordField('Confirm Your Password', validators=[DataRequired(), EqualTo('password',    message='Passwords must match.')])

    submit_button = SubmitField()

class UserLoginForm(FlaskForm,UserMixin):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class CreateCharacter(FlaskForm):
    name = StringField('Character Name', validators=[DataRequired()])
    description = StringField('Description')
    movies = StringField('Movies')
    events = StringField('Events')
    series = StringField('Series')
    powers = StringField('Powers')
    snapped = RadioField('Snapped', coerce=bool, choices=[('value','Yes'),('value_two','No')], default='value_two')
    submit_button = SubmitField()