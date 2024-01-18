from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from __init__ import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

"""this module implement an ORM for SQLAlchemy"""

class User(db.Model, UserMixin):    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    activities = db.relationship('Activity', backref='user', lazy=True)
    
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    

