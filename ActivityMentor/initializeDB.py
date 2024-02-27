from __init__ import db, app
from models import User, Activity
from datetime import date


"""use this module to initialize db"""


class sampleDBmanager():
    
    
    def __init__(self):
        pass
    
    def createTables(self):
        with app.app_context():
            db.create_all()
            
    def clear_data(self):
        with app.app_context():
            db.session.query(User).delete()
            db.session.query(Activity).delete()
            db.session.commit()
            

DB = sampleDBmanager()

#RUN THIS FUNCTION 
DB.createTables()

#DB.add_data()
#DB.clear_data()
#DB.view_data()
