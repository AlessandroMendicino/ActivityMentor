from flask import (Flask, render_template, 
                request, flash,
                url_for, redirect,
                session, Blueprint)
from APIclient import copilot_chat_prompt
import json
from models import User, Activity
from __init__ import db
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from datetime import datetime

    

""" This module implement login and signup routes"""

auth = Blueprint('auth', __name__)


@auth.route('/')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['GET','POST'])
def login_post():
    #For GET requests, display the login form. 
    #For POSTS, login the current user by processing the form.
    
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('main.activityHome'))
        else:
            flash("wrong email or password!")
            return redirect(url_for('auth.login'))
        

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    #TODO: add check password confirmed
    #TODO: add tutor/stage status
    
    # code to validate and add user to database goes here
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if username and email and password:
        try:
            # create a new user with the form data. Hash the password so the plaintext version isn't saved.
            new_user = User(username=username, email=email)
            new_user.set_password(password)

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()
        except:
            flash('Email address already exists')
            return render_template('signup.html')
    else:
        flash('do not enter empty fields')
        return render_template('signup.html')
        
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user(current_user)
    session.clear()
    return redirect(url_for('login'))

@auth.route('/profile')
@login_required
def profile():
    return '<H1> PROFILE WORK IN PROGRESS </H1>' #TODO add profile template
