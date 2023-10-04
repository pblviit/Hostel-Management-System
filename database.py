from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


class student_login(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(400), nullable = False)

class admin_login(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)

with app.app_context():
    db.create_all()

temp = admin_login(email = 'asdfsdf', password = 'asdfeanasfd' )
db.session.add(temp)
db.session.commit()

