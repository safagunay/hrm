from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    send_file
)
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from flaskr.extensions import db, depot
from flaskr.models import User, Candidate, db
from flaskr.blueprints.forms import LoginForm

bp = Blueprint('Admin', __name__)

@bp.route('/admin/file', methods=['GET'])
#@login_required
def file():
    fileid = request.args.get('fileid')
    if fileid:
        stored_file = depot.get(fileid)
        if stored_file:
            return send_file(
                stored_file,
                mimetype=stored_file.content_type,
            )
            
        flash("File not found!")
    else:
        flash("Specify file id!")
    return redirect(url_for("Admin.admin"))

@bp.route('/admin', methods=('GET', 'POST'))
#@login_required
def admin():
    candidates = Candidate.query.all()
    return render_template("admin.html", candidates=candidates)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            error = None
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user is None:
                error = "Invalid username !"
            elif not check_password_hash(
                user.password,
                password
            ):
                error = "Invalid password !"
            if error is None:
                login_user(user)
                next = request.args.get('next')
                return redirect(next or url_for('Admin.admin'))
            flash(error)
        else:
            flash("Invalid form data")
    return render_template('login.html', form=form)