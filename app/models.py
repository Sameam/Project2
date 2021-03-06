from app import db
from app import login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# users model 
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(128), index=True, unique=True)
    phone = db.Column(db.Integer, unique=True)
    admin = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    score_1 = db.Column(db.Integer)
    score_2 = db.Column(db.Integer)
    score_3 = db.Column(db.Integer)
    feedback = db.Column(db.String(128))


    def __repr__(self):
        return '<User {}>'.format(self.name) 
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


        

        
    
        

    
    
    
