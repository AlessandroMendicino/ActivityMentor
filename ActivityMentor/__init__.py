import sys
from os.path import abspath, dirname

# Aggiungi la directory del progetto al percorso di ricerca di Python
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

# Configurazione, inizializzazione dell'app e del database, registrazione dei blueprint e del login manager

app = Flask(__name__, template_folder=os.path.abspath("./ActivityMentor/templates"), static_folder=os.path.abspath("./ActivityMentor/static"))
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ActivityMentor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.abspath("./ActivityMentor/uploads")
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}
db.init_app(app)

login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))
