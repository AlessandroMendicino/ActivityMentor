from flask import Flask, render_template, request
from APIclient import simple_chat_prompt
import json
from __init__ import app, db

@app.route('/')
def index():
    return render_template('index.html', last_activity="Ultima Attività:", last_date="Ultima Data:")

@app.route('/add_activity', methods=['POST'])
def add_activity():
    activity = request.form.get('activity')
    date = request.form.get('date')

    # Esegui la logica per aggiungere l'attività al tuo database
    # Aggiorna last_activity e last_date in base ai dati effettivi nel tuo database

    return render_template('index.html', last_activity=f"Ultima Attività: {activity}", last_date=f"Ultima Data: {date}")

@app.route('/show_all_activities')
def show_all_activities():
    # Esegui la logica per ottenere tutte le attività dal tuo database
    # Passa i dati a Jinja e aggiorna la pagina

    return render_template('index.html', last_activity="Ultima Attività:", last_date="Ultima Data:")

@app.route('/search_by_month')
def search_by_month():
    month = request.args.get('month')

    # Esegui la logica per ottenere le attività per il mese specificato dal tuo database
    # Passa i dati a Jinja e aggiorna la pagina

    # Ad esempio, restituisci tutte le attività del mese specificato per ora
    activities_for_month = []  # Implementa la tua logica qui

    return render_template('index.html', last_activity="Ultima Attività:", last_date="Ultima Data:", activities=activities_for_month)

if __name__ == "__main__":
    app.run(debug=True)