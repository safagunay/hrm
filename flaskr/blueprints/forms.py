from flask_wtf import FlaskForm
from wtforms import StringField, FileField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileRequired

class LoginForm(FlaskForm):
    username = StringField('First Name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class ApplicationForm(FlaskForm):
    cv_file = FileField(validators=[FileRequired()])
    first_name = StringField('First Name', validators=[InputRequired(), Length(max=20)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=20)])
    email = StringField('Email', validators=[Email(), InputRequired(), Length(max=50)])

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    pwd = PasswordField('Password', validators=[InputRequired(), 
        EqualTo('confirm_pwd', message="Passwords must match"),
        Length(min=6, max=20)])
    confirm_pwd = PasswordField('Confirm Password')
    remember_me = BooleanField()
