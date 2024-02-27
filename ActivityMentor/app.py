from __init__ import app

def blueprints():
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

#for merge
# Esecuzione dell'app web
if __name__ == "__main__":
    blueprints()
    app.run(debug=True)


