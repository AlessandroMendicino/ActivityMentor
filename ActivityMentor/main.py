from flask import (Flask, render_template, 
                request, flash,
                url_for, redirect,
                session, Blueprint)
from APIclient import copilot_chat_prompt
import json
from models import User, Activity
from app import db
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from datetime import datetime


"""TODO:
- risolvere problemi sessione utente
- aggiungere gestione admin/utentiStandard
- aggiungere excell doc generator
"""

main = Blueprint('main', __name__)





"""add new activity for current user """

@main.route('/index', methods=['GET', 'POST'])
@main.route('/activityHome', methods=['GET','POST'])
@login_required
def activityHome():
    #TODO: bugfix no date event
    
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
    return render_template('index.html')
    


"""view all activity for current-user"""

@main.route('/viewActivity')
@login_required
def viewActivity():
    user = User.query.filter_by(id=current_user.id).first()
    activities = Activity.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', activities=activities)




""" AiCopilot function call """

@main.route('/AiCopilot', methods=["GET", "POST"])
@login_required
def AiCopilot():
    response = None
    
    if request.method == "POST":
        activities = Activity.query.filter_by(user_id=current_user.id).all() #current_id on function
        result_string = '\n'.join([f'{result.date}: {result.description}' for result in activities])
        input_utente = request.form["input_utente_chat"]
        response = copilot_chat_prompt(input_utente, result_string)
        print(input_utente)
        print(response)
            #return render_template('index.html', response=response)
            
    return render_template("index.html", response=response, hide_spinner=True)
    
    




