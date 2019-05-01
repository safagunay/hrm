import sys

from werkzeug.security import generate_password_hash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from depot.manager import DepotManager
from migrate import Candidate


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_pyfile('config.py', silent=False)
    
    db = SQLAlchemy(app)
    
    number = 0
    if len(sys.argv) > 1 :
        try:
            number = int(sys.argv[1])
        except:
            pass
    
    if number:
        DepotManager.configure('default', { 
            'depot.storage_path': '../../files'
        })
        depot = DepotManager.get()
        fileid = depot.create(open('fake.txt','br'))
        for i in range(number):
            candidate = Candidate(
                first_name = "User%d" % i,
                last_name = "Userlastname%d" %i,
                email = "useremail%d@hrm.com" %i,
                cv_fileid = fileid
            )
            db.session.add(candidate)
            db.session.commit()
        print("Fake candidate data is inserted(%d times)" %number)