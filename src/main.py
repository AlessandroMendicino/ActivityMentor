from flask import (Flask, render_template, 
                request, flash,
                url_for, redirect,
                session, Blueprint)
from APIclient import simple_chat_prompt
import json
from __init__ import db, create_app
#from __initi__ import app, db
from DBmanager import User, Activity
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from datetime import datetime


"""TODO:
- risolvere problemi sessione utente
- aggiungere gestione admin/utentiStandard
- implementazione IA
- implementazione ricerca per mese (opzionale)"""

app = create_app()


@app.route('/profile')
@login_required
def profile():
    return 'Profile'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login_post():
    """For GET requests, display the login form. 
    For POSTS, login the current user by processing the form."""
    
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('activityHome'))
        else:
            flash("wrong email or password!")
            return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

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
        
    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user(current_user)
    session.clear()
    return redirect(url_for('login'))





"""app feature - route """



##add new activity for current user 

@app.route('/index', methods=['GET', 'POST'])
@app.route('/activityHome', methods=['GET','POST'])
@login_required
def activityHome():
    
    activity = None
    date_activity = None
    username = None

    if request.method=='POST':
        user = User.query.filter_by(id=current_user.id).first()
        username = user.username
        activity = request.form['activityInput']
        date_activity = request.form['dateInput']
        date_object = datetime.strptime(date_activity, '%Y-%m-%d').date() #for db 
        if username and activity and date_activity:
            new_activity = Activity(date=date_object, description=activity, user_id=current_user.id)
            db.session.add(new_activity)
            db.session.commit()
        
    return render_template('index.html', activity=activity, date_activity=date_activity, username=username)


#view all activity for current-user

@app.route('/viewActivity')
@login_required
def viewActivity():
    user = User.query.filter_by(id=current_user.id).first()
    activities = Activity.query.filter_by(user_id=current_user.id).all()
    for act in activities:
        print(act.description, act.date)
    return render_template('index.html', activities=activities)






'''   
@app.route('/show_all_activities')
    def show_all_activities():
    pass
     Esegui la logica per ottenere tutte le attività dal tuo database
    Passa i dati a Jinja e aggiorna la pagina

    #return render_template('index.html', last_activity="Ultima Attività:", last_date="Ultima Data:")
'''

#@app.route('/show_all_user')
#def show_all_user():
    #pass

'''
@app.route('/search_by_month')
def search_by_month():
    month = request.args.get('month')

     Esegui la logica per ottenere le attività per il mese specificato dal tuo database
     Passa i dati a Jinja e aggiorna la pagina

     #d esempio, restituisci tutte le attività del mese specificato per ora
    activities_for_month = []  # Implementa la tua logica qui

    return render_template('index.html', last_activity="Ultima Attività:", last_date="Ultima Data:", activities=activities_for_month)
'''


if __name__ == "__main__":
    app.run(debug=True)