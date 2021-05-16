from app import app, db
from flask import render_template, url_for,request,flash,redirect
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm, RegistrationForm, editForm
from app.models import Users
from werkzeug.urls import url_parse
from datetime import datetime

# render opening html
@app.route("/")
def index():
    return render_template("opening.html",title="Home")

# render content html
@app.route("/content")
@login_required
def content():
    return render_template("content.html", title="Descriptive Statistics")

# render inferential html
@app.route("/inferential")
@login_required
def inferential():
    return render_template("inference.html", title="Inference Statistics")

# login route
@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        users = Users.query.filter_by(name=form.name.data).first()
        if users is None:
            flash('Your name is wrong, please input correctly name')
            return redirect(url_for('login'))
        elif not users.check_password(form.password.data):
            flash('Your password is wrong, please input correctly password')
            return redirect(url_for('login'))
        login_user(users, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('introduction')
        return redirect(next_page)
    return render_template("login.html", title="Login", form = form)

# registration route
@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        users = Users(name=form.name.data, email=form.email.data, phone=form.telephone.data)
        users.set_password(form.password.data)
        db.session.add(users)
        db.session.commit()
        flash('Congratulations, you are now a registered users!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = form)

# render log out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

# render progress html 
@app.route("/progress")
@login_required
def progress():
    return render_template("progress.html", title="Progress",user=current_user.name)

# render result page
@app.route("/result")
@login_required
def result():
    if current_user.admin == True:
        users = Users.query.filter(Users.admin != True).all()
        return render_template("result.html", title="Result",name= current_user.name, id = current_user.id,users = users)
    return render_template("result.html", title="Result",name= current_user.name, id= current_user.id)

# # edit Users in a database 
@app.route('/result/edit/<int:user_id>', methods=['GET','POST'])
@login_required
def edit_users(user_id):
    user = current_user
    if user.admin:
        form = editForm()
        student = Users.query.filter(Users.id==user_id).first()
        if form.validate_on_submit():
            student.name = form.name.data
            student.name = form.name.data
            student.score_1 = form.score_1.data
            student.score_2 = form.score_2.data
            student.score_3 = form.score_3.data
            student.feedback = form.feedback.data
            db.session.commit()
            return redirect(url_for('result'))  
    return render_template('edit.html',title="Edit", form=form)

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

# delete Users from the database
@app.route('/delete/<user_id>')
@login_required
def delete(user_id):
    users = Users.query.filter(Users.id == user_id).first()
    db.session.delete(users)
    db.session.commit()
    return redirect(url_for('result'))

# get Users score 1 
@app.route('/score1',methods = ['GET','POST'])
@login_required
def score1():
    requestArgs = request.values  
    score1 = requestArgs.get("score")
    users = current_user
    users.score_1 = score1
    users.timestamp = datetime.utcnow()
    db.session.commit()
    return render_template("quiz_intro.html", title="Quiz", name=current_user.name)

# get Users score 2 
@app.route('/score2',methods = ['GET','POST'])
@login_required
def score2():
    requestArgs = request.values  
    score2 = requestArgs.get("score")
    users = current_user
    users.score_2 = score2
    users.timestamp = datetime.utcnow()
    db.session.commit()
    return render_template("quiz_intro.html", title="Quiz", name=current_user.name)

# get Users score 3 
@app.route('/score3',methods = ['GET','POST'])
@login_required
def score3():
    requestArgs = request.values  
    score3 = requestArgs.get("score")
    users = current_user
    users.score_3 = score3
    users.timestamp = datetime.utcnow()
    db.session.commit()
    return render_template("quiz_intro.html", title="Quiz", name=current_user.name) 