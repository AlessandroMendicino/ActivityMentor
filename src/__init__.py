from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

# create the app
app = Flask(__name__, template_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\templates")

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///STAGEACTS.db"
app.config['SECRET_KEY'] = 'secret'


# initialize the app with the extension
db.init_app(app)