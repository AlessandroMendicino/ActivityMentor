from tinydb import TinyDB

"""this class implement a simple embedded db nosql with tinydb"""

class activitiesStorage():

    def __init__(self):
        self.db_name = "storage.json"
        self.db = TinyDB(self.db_name)


    def add_data(self, date, activity):
        to_insert_data = {"DATA" : date, "ATTIVITA'" : activity}
        self.db.insert(to_insert_data)
       
    def clear_data(self):
        self.db.truncate()
    
    def view_data(self):
        return self.db.all()

    def search_month():
        pass


