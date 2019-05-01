from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.extensions import db, depot
from flaskr.models import Candidate, db
from flaskr.blueprints.forms import ApplicationForm
from flaskr.extensions import depot

bp = Blueprint('Index', __name__)

def is_unique_email(email):
    return not Candidate.query.filter_by(email=email).first()

@bp.route('/', methods=('GET', 'POST'))
def register():
    form = ApplicationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if not is_unique_email(form.email.data):
                return "Email used before!"
            cv_file = form.cv_file.data
            file_id = depot.create(cv_file)
            candidate = Candidate(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                email = form.email.data,
                cv_fileid = file_id
            )
            db.session.add(candidate)
            db.session.commit()
            return "Success"

        return "Invalid form data"
    return render_template('index.html', form=form)