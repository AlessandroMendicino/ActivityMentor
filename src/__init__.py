#from ast import main
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\templates", static_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\static")


    app.config['SECRET_KEY'] = os.urandom(32) #dot not send this in production src code, use ambient variable
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///STAGEACTS.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    db.init_app(app)
    
    login_manager.session_protection = "strong"
    login_manager.login_view = 'login'
    login_manager.init_app(app)
    

    return app

app = create_app()

from models import User
    
@login_manager.user_loader
def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
    
from main import main as main_blueprint
app.register_blueprint(main_blueprint)