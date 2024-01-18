from __init__ import db, app
from DBmanager import User, Activity
from datetime import date


"""use this module to initialize db"""

class sampleDBmanager():
    
    
    def __init__(self):
        pass
    
    def createTables(self):
        with app.app_context():
            db.create_all()
    
    
    def add_data(self): #use this function to insert sample data 
        with app.app_context():
            me = User(username='alessandro', email="alessandro@sample.com", is_admin=True)
            me.set_password("ciao")
            you = User(username="MarioRossi", email="mariorossi@sample.com", is_admin=True)
            you.set_password("minchia")
            studio1 = Activity(date=date(2024, 1, 1), description="studio software", user=you)
            studio2 = Activity(date=date(2024, 2, 2), description="studio libri", user=you)
            db.session.add(me)
            db.session.commit()
            db.session.add(you)
            db.session.commit()
            db.session.add(studio1)
            db.session.commit()
            db.session.add(studio2)
            db.session.commit()
    
    
    def clear_data(self):
        with app.app_context():
            db.session.query(User).delete()
            db.session.query(Activity).delete()
            db.session.commit()
      
    def view_data(self): #query sample
        with app.app_context():
            attività = Activity.query.filter(db.extract('month', Activity.date) == 2).all()
        for act in attività:
            print(act.id, act.date, act.description) 
    


"""use this module for testing and debug"""

DB = sampleDBmanager()

DB.createTables()
#DB.add_data()
#DB.clear_data()
#DB.view_data()
