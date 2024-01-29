from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
import os


# Configurazione, inizializzazione dell'app e del database, registrazione dei blueprint e del login manager

app = Flask(__name__, template_folder=os.path.abspath("./ActivityMentor/templates"), static_folder=os.path.abspath("./ActivityMentor/static"))
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ActivityMentor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  
login_manager = LoginManager(app)

login_manager.session_protection = "strong"
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))
