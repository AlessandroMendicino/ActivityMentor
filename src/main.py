from storage import activitiesStorage

DB = activitiesStorage()

"""main class that control data flows"""

class dataController():

    def __init__(self):
        pass

    def insert_data(self, date, activity):
        DB.add_data(date, activity)
        print("successfull insert")

    def clear(self):
        DB.clear_data()
        
    def view(self):
        DB.view_data()

if __name__ == "__main__":

    DC = dataController()

    while True:
        response = input("insert record? type y o n: ")
        if response == "y":
            date = input("insert date: ")
            activity = input("insert activity: ")
            DC.insert_data(date, activity)
        else:
            break
    
    while True:
        response = input("view - clear - exit: ")
        if response == "view":
            DC.view()
        elif response == "clear":
            DC.clear()
        elif response == "exit":
            break


