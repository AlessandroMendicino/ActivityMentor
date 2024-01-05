from tinydb import TinyDB

"""this class implement a simple embedded db nosql with tinydb"""

class activitiesStorage():

    def __init__(self):
        self.db_name = "storage.json"
        self.db = TinyDB(self.db_name)


    def add_data(self, date, activity):
        to_insert_data = {"DATA" : date, "ATTIVITA'" : activity}
        self.db.insert(to_insert_data)
    
    #sto facendo un inserimento sample di dati, ipotizzando alcune attività del mese di febbraio
    #def add_data(self):
        #dati_da_inserire = [{"mese" :  "Febbraio", "Attività" : "programmazione ad oggetti" },
                             #{"mese" : "Febbraio", "Attività" : "erediterietà e polimorfismo" },
                             #{"mese" : "Febbraio", "Attività" : "software design pattern" },
                             #{"mese" : "Febbraio", "Attività" : "esercitazioni con programmazione ad oggetti in python" },
                             #{"mese" : "Febbraio", "Attività" : "esercitazioni design patterns" },
                             #{"mese" : "Febbraio", "Attività" : "singleton e abstractFacotry methods in python" },
                             #{"mese" : "Febbraio", "Attività" : "riepilogo ed approfondimento programmazione ad oggetti" },
                             #{"mese" : "Febbraio", "Attività" : "lavoro su caso d'uso, python." },
                             #{"mese" : "Marzo", "Attività" : "introduzione a CI/CD" },
                             #{"mese" : "Marzo", "Attività" : "esempi continuous integration ed esercitazioni" },
                             #{"mese" : "Marzo", "Attività" : "esempi continuous deployement ed esercitazioni" },
                             #{"mese" : "Marzo", "Attività" : "Introduzione a jenkins, github actions" },
                             #{"mese" : "Marzo", "Attività" : "docker" },
                             #{"mese" : "Marzo", "Attività" : "webinar iA Generativa" },
                             #{"mese" : "Marzo", "Attività" : "lavoro su caso d'uso python" },
                             #{"mese" : "Marzo", "Attività" : "deployement di una build su server nexus locale" },
                             #{"mese" : "Marzo", "Attività" : "esercitazioni CI/CD" },
                            #]

        #self.db.insert_multiple(dati_da_inserire)
    
    def clear_data(self):
        self.db.truncate()
    
    def view_data(self):
        for item in self.db:
            return item

    def search_month():
        pass


