
# Flask Import
from flask import Flask, abort, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap5

# sql import
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey, Integer

# form import
from forms import student_form, admin_form, registration_form

# creating app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
Bootstrap5(app)

# creating database
db = SQLAlchemy()
db.init_app(app)

# ------------------------------------------------ Database tables
# class Admin(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     email = db.Column("temp",db.String(100))
#     password = db.Column(db.String(100))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(200), nullable = False)
    dob = db.Column(db.String(200), nullable = False)
    mobileno = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(200), nullable = False)
    address = db.Column(db.String(255), nullable = False)
    
class Room(db.Model):
    roomno = db.Column(db.Integer, primary_key = True)
    roomcapacity = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    type = db.Column(db.Integer)
    id = db.Column(db.Integer)

class Allocation(db.Model):
    allocation_id = db.Column(db.Integer, primary_key = True)
    check_in = db.Column(db.String(10))
    check_out = db.Column(db.String(10))
    student_id = db.Column(db.Integer)
    room_no = db.Column(db.Integer)

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Integer)
    payment_date = db.Column(db.String(10))
    student_id = db.Column(db.Integer)



with app.app_context():
    db.create_all()


# ================================================= Page routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/login/admin", methods = ["POST", "GET"])
def admin_login():
    form = admin_form()
    if form.validate_on_submit():
        if (request.form.get('email') == "password" and request.form.get('password') == "password"):
            return "Submited Successfully"
        else:
            return "Unsuccessfull"
    return render_template("admin_login.html", form = form)

@app.route("/login/student", methods = ["POST", "GET"])
def student_login():
    form = student_form()
    if form.validate_on_submit():
        return redirect(url_for('register_page'))
    return render_template("student_login.html", form = form)

@app.route("/register", methods = ["POST", "GET"])
def register_page():
    form = registration_form()
    if form.validate_on_submit():
        # print(request.form.get('email'))
        temp = Student(
            name = request.form.get('Name'),
            dob = request.form.get('DOB'),
            email = request.form.get('email'),
            mobileno = request.form.get('mobileno'),
            address = request.form.get('address')
        )
        db.session.add(temp)
        db.session.commit()
        return "Registered Successfully"
    return render_template("registration.html", form = form)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
