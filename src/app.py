from flask import Flask, render_template, request, flash, url_for, redirect, session
from APIclient import simple_chat_prompt
import json
from __init__ import app, db
from DBmanager import User, Activity
from werkzeug.security import check_password_hash



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        
        #TODO AGGIUNGERE IS_ADMIN
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('account creato con successo!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash('Login effettuato', 'success')
            return redirect(url_for('add_activity'))
        else:
            flash('Credenziali non valide', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logout effettuato con successo!', 'success')
    return redirect(url_for('login'))


@app.route('/add_activity', methods=['POST'])
def add_activity():
    if 'user_id' in session:
        user = db.Query.filter(id=session['user_id'])
        username = user.username
        print(username)
        activity = request.form.get('activity')
        date = request.form.get('date')
        
        new_activity = Activity(date=date, description=activity, user_id=session['user_id'])
        
        return render_template('index.html', activity=activity, date=date, username=username)

    flash('effettua login!', 'warning')
    return redirect(url_for('login'))
    

   
@app.route('/show_all_activities')
def show_all_activities():
    pass
    # Esegui la logica per ottenere tutte le attività dal tuo database
    # Passa i dati a Jinja e aggiorna la pagina

    #return render_template('index.html', last_activity="Ultima Attività:", last_date="Ultima Data:")

@app.route('/show_all_user')
def show_all_user():
    pass

#@app.route('/search_by_month')
#def search_by_month():
    #month = request.args.get('month')

    # Esegui la logica per ottenere le attività per il mese specificato dal tuo database
    # Passa i dati a Jinja e aggiorna la pagina

    # Ad esempio, restituisci tutte le attività del mese specificato per ora
    #activities_for_month = []  # Implementa la tua logica qui

    #return render_template('index.html', last_activity="Ultima Attività:", last_date="Ultima Data:", activities=activities_for_month)



if __name__ == "__main__":
    app.run(debug=True)