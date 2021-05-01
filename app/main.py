from app import app
from flask import Flask,render_template, url_for,request,flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("opening.html",title="Home")

@app.route("/content")
def content():
    return render_template("content.html", title="Content")

@app.route("/login")
def login():
    return render_template("register.html", title="Register")

@app.route("/templates/register",method=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('name')
        password = request.form.get('pwd')
        password2 = request.form.get('pwd2')
        #email , phone
        if not all([username,password,password2]):
            flash('Please complete your information')
        elif password != password2:
            flash ('The two passwords entered are inconsistent, please enter them again')
        else:
            return 'password is correct'
            
    return render_template('register.html')


