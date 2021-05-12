from app import app, db
from flask import render_template, url_for,request,flash,redirect
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse


@app.route("/")
@app.route("/index")
def index():
    return render_template("opening.html", title="Home")

@app.route("/content")
def content():
    return render_template("content.html", title="Content")

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None:
            flash('Your name is wrong, please input correctly name')
            return redirect(url_for('login'))
        elif not user.check_password(form.password.data):
            flash('Your password is wrong, please input correctly password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title="Login", form = form)

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, phone=form.telephone.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

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

@app.route("/introduction")
@login_required
def introduction():
    return render_template("introduction.html", title="Introduction",name=current_user.name)

@app.route("/quiz")
@login_required
def quiz():
    return render_template("quiz_intro.html", title="Quiz", name=current_user.name)

@app.route("/beginner")
@login_required
def beginner():
    return render_template("beginner.html", title="Beginner", name=current_user.name)

@app.route("/intermediate")
@login_required
def intermediate():
    return render_template("intermediate.html", title="Intermediate", name= current_user.name)

@app.route("/advance")
@login_required
def advance():
    return render_template("advance.html", title="Advance", name=current_user.name)  

