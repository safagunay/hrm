from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required
from flaskr.extensions import db, depot
from flaskr.models import User, Candidate

from flask_wtf import FlaskForm
from wtforms import StringField, FileField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo, Length

bp = Blueprint('index', __name__)

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    pwd = PasswordField('Password', validators=[InputRequired(), 
        EqualTo('confirm', message="Passwords must match"),
        Length(min=6, max=20)])
    confirm_pwd = PasswordField('Confirm Password')
    remember_me = BooleanField()
    # cv_file = FileField('Cv Document',validators=[DataRequired()])

@bp.route('/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return "Success"
        return "Fail"
    return render_template('index.html', form=form)