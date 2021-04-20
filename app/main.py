from app import app
from flask import render_template, url_for

@app.route("/")
def index():
    return render_template("opening.html",title="Home")

@app.route("/content")
def content():
    return render_template("content.html", title="Content")