from app import db 
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    email = db.Column(db.String(100), index=True)
    password = db.Column(db.String(100))
    phone = db.Column(db.Integer, unique=True)
    
    def __repr__(self):
        return "<User {}>".format(self.name)
    
    @login.user_loader
    def load_user(id):
        return Users.query.get(int(id))
    
    
    
