
from flask import Flask, render_template, request
from storage import activitiesStorage

app = Flask(__name__, template_folder=r"C:\Users\alessandro.mendicino\PYTHON_PROJECTS\STAGEACTS\src\templates")
DB = activitiesStorage()

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    attivita = None
    activities_list = []  # Inizializza con i dati correnti

    if request.method == "POST":
        data = request.form["data"]
        attivita = request.form["attivita"]
        DB.add_data(data, attivita)
    activities_list = DB.view_data()  # Aggiorna con i nuovi dati

    return render_template("index.html", activities_list=activities_list, data=data, attivita=attivita)

if __name__ == '__main__':
    app.run(debug=True)
