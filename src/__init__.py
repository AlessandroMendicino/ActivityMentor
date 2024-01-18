from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\templates", static_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\static")

    app.config['SECRET_KEY'] = os.urandom(32) #dot not send this in production src code, use ambient variable
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///STAGEACTS.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.session_protection = "strong"
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    from DBmanager import User
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))


    return app




#create the app
#app = Flask(__name__, template_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\templates", static_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\static")

#configure the SQLite database, relative to the app instance folder
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///STAGEACTS.db"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'secret'

#db= SQLAlchemy()

#initialize the app with the extension
#db.init_app(app)

#init SQLAlchemy so we can use it later in our models
#db = SQLAlchemy()
