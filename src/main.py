from storage import activitiesStorage
import json
from APIclient import simple_chat_prompt

DB = activitiesStorage()

"""main class that control data flows, use it for debug"""

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
    
    while True:
        response = input("view - clear - exit - Ai - insert: ")
        if response == "view":
            elementi = DB.view_data()
            print(type(elementi))
            #for element in elementi:
                #listaKey = element.keys()
                #listaValues = element.values()
                #print(list(listaKey)[0] + " " + list(listaValues)[0] + " // " 
                       #+  list(listaKey)[1] + " " 
                       #+ list(listaValues)[1])
           
            #molto meglio ->
            for dato in elementi:
                for attribute, value in dato.items():
                    print(attribute + " " + value)
                             
  
            
        elif response == "insert":
            DC.insert_data()
        elif response == "clear":
            DC.clear()
        elif response == "exit":
            break
        elif response == "Ai":
            iA_input = json_to_string()
            response = simple_chat_prompt(iA_input)
            print(response)
            break



