from app import app, db
from flask import render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Users
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
def index():
    return render_template("opening.html",title="Home")

@app.route("/content")
@login_required
def content():
    return render_template("content.html", title="Content")

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = Users.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return redirect(url_for("login"))
    
    login_user(user) 
    return redirect(url_for("content"))

@app.route("/signup")
def signup():
    return render_template("register.html", title="Signup")

@app.route("/signup", methods=["POST"])
def signup_post():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    
    
    user = Users.query.filter_by(email=email).first() # get the first row in the table that has the email
    if user: 
       return redirect(url_for("signup"))
   
    new_user = Users(name=name,email=email, password=generate_password_hash(password, method="sha256"),phone=phone) # create a new user object
    db.session.add(new_user) # add user into the database 
    db.session.commit() # commit 
    
    return redirect(url_for("login"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/asessment")
@login_required
def asessment():
    return render_template("asessment.html", title="Quiz")

@app.route("/progress")
@login_required
def progress():
    return render_template("progress.html", title="Progress",user=current_user.name)

@app.route("/result")
@login_required
def result():
    return render_template("result.html", title="Result",name= current_user.name, id= current_user.id)

@app.route("/user")
@login_required 
def user():
    return render_template("user.html", title="User", name=current_user.name, id=current_user.id)
    