from storage import activitiesStorage
import json
from APIclient import simple_chat_prompt
from rich.console import Console

console = Console()
DB = activitiesStorage()

"""main class that control data flows"""

#gestore dei dati, inserisce, elimina e visualizza i dati del dbJson
class dataController():

    def __init__(self):
        pass

    def insert_data(self): 
        DB.add_data() 
        print("successfull insert")

    def clear(self):
        DB.clear_data()
        
    def view(self):
        DB.view_data()


#trasformo il file json del tinydb in stringa da passare al modello
def json_to_string():
    with open('storage.json' , 'r') as file:
        contenuto_json = json.load(file)
    stringa_json = json.dumps(contenuto_json, indent=2) 
    return stringa_json


if __name__ == "__main__":

    DC = dataController()

#gestione input output da riga di comando
    
    #while True:
        #response = input("insert record? type y o n: ")
        #if response == "y":
            #date = input("insert date: ")
            #activity = input("insert activity: ")
            #DC.insert_data(date, activity)
        #else:
            #break
    
    while True:
        response = input("view - clear - exit - Ai - insert: ")
        if response == "view":
            DC.view()
        elif response == "insert":
            DC.insert_data()
        elif response == "clear":
            DC.clear()
        elif response == "exit":
            break
        elif response == "Ai:":
            iA_input = json_to_string()
            response = simple_chat_prompt(iA_input)
            print(response)



