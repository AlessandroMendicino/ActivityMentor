from flask import Flask, render_template, request
from storage import activitiesStorage
from flask_socketio import SocketIO, emit
from APIclient import simple_chat_prompt
import json

app = Flask(__name__, template_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\templates")
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
DB = activitiesStorage()

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    attivita = None

    if request.method == "POST":
        data = request.form["data"]
        attivita = request.form["attivita"]
        DB.add_data(data, attivita)

    activities = DB.view_data()
    listaDate = []
    listaAttivita = []
    for item in activities:
        listaDate.append(item["DATA"])
        listaAttivita.append(item["ATTIVITA'"])
    
    print(listaDate)
    print(listaAttivita)
    return render_template("index.html", listeElementi=zip(listaAttivita, listaDate), listaDate=listaDate, data=data, attivita=attivita)

#TODO implements this function in frontend
@app.route('/start_analysis')
def start_analysis():
    
    def json_to_string():
        with open('storage.json' , 'r') as file:
            contenuto_json = json.load(file)
            stringa_json = json.dumps(contenuto_json, indent=2) 
        return stringa_json

    # Esegui l'analisi AI qui e restituisci il risultato
    result = simple_chat_prompt(json_to_string())
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)