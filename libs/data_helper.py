import json
import random

path = "./data/data.json"

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as open_file:
        json.dump(data, open_file, indent=4)

#Funktion um Json-Dateien zu laden
def load_json(path):
    try:
        with open (path) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        data = {}
        return data

#Funktion um einen Monat zu speichern:
def month_save(month, year):
    #Versuch Json auszulesen
    name = str(month) + str(year)
    data = load_json(path)
    if name in data:
        return
    else:
        data[name] = {
            "expenses": {}, "income":{}
        }
    save_json(path,data)


#Funktion um einen Monat zu bearbeiten:
def month_update():
    return


#Funktion um einen Monat in der Übersicht anzuzeigen:
def month_show_overview():
    return



#Funktion um Kosten hinzuzufügen:
def expenses_add(month,year,amount,title,path):
    name = str(month) + str(year)
    key = int(name + str(random.randrange(0, 1000)))
    

    data = load_json(path)
    
    #print(data[name][0]["expenses"])
    data[name]["expenses"][key] = { 'amount': str(amount), 'title': str(title)}
    
    save_json(path, data)


    return


#Funktion um Kosten zu löschen:
def cost_delete():
    return


#Funktion um Einnahmen hinzuzufügen:
def earnings_add(month,year,amount,title,path):
    name = str(month) + str(year)
    key = int(name + str(random.randrange(0, 1000)))
    #income = key: { 'amount': str(amount), 'title': str(title)}

    data = load_json(path)
    
    #print(data[name][0]["expenses"])
    data[name][0]["income"][key] = "{ 'amount': str(amount), 'title': str(title)}"
    
    save_json(path, data)


    return
month_save(11,2019)
expenses_add(11,2019,30,"test2",path)

#Funktion um Einnahmen zu löschen:
def earnings_delete():
    return


#Funktion um Einnahmen & Kosten eines Monats als Summe zu berechnen:
def calculate_month():
    return


#Funktion um Monat zu löschen:
def month_delete():
    return