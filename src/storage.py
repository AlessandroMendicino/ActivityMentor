from tinydb import TinyDB


class activitiesStorage():
    def __init__(self):
        self.db_name = "storage.json"
        self.db = TinyDB(self.db_name)
        
    def add_data(self, date, act):
        DB = self.db
        DB.insert({date : act})
    

    def clear_data(self):
        self.db.truncate()
    
    def view_data(self):
        for item in self.db:
            print(item)


if __name__ == "__main__":

    database = activitiesStorage()

    database.add_data(21, "ciaociao")
    database.add_data(99, "eheheh")
    database.add_data(200, "ghghgh")

    database.view_data()