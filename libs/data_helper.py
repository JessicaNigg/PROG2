import json
import random

path = "./data/data.json"

#Funktion um Json-Dateien zu speichern
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
            "expenses": {}, "income":{}, "balance": "0"
        }
    save_json(path,data)


#Funktion um einen Monat zu bearbeiten:
def expenses_update(path,key,month,year,amount,title):
    expenses_delete(path,key,month,year)
    expenses_add(month,year,amount,title,path)

    return
#HTML-Formular erstellen mit bereits ausgefüllten Feldern


#Funktion um einen Monat in der Übersicht anzuzeigen:
def month_show_overview():
    return



#Funktion um Kosten hinzuzufügen:
def expenses_add(month,year,amount,title,path):
    name = str(month) + str(year)
    key = int(name + str(random.randrange(0, 1000)))
    

    data = load_json(path)
    data[name]["expenses"][key] = { 'amount': str(amount), 'title': str(title)}
    
    save_json(path, data)
    decrease_balance(amount,month,year,path)


    return


#Funktion um Kosten zu löschen:
def expenses_delete(path,key,month,year):
    try:
        name = str(month) + str(year)
        data = load_json(path)
        key = str(key)
        amount = data[name]["expenses"][key]["amount"]
        data[name]["expenses"].pop(str(key))
        save_json(path,data)
        increase_balance(amount,month,year,path)
        return
    except:
        return


#Funktion um Einnahmen hinzuzufügen:
def earnings_add(month,year,amount,title,path):
    name = str(month) + str(year)
    key = int(name + str(random.randrange(0, 1000)))

    data = load_json(path)
    
    
    data[name]["income"][key] = { 'amount': str(amount), 'title': str(title)}
    
    save_json(path, data)

    increase_balance(amount,month,year,path)

    return



#Funktion um Einnahmen zu löschen:
def earnings_delete(path,key,month,year):
    try:
        name = str(month) + str(year)
        data = load_json(path)
        key = str(key)
        amount = data[name]["income"][key]["amount"]
        data[name]["income"].pop(str(key))
        save_json(path,data)
        decrease_balance(amount,month,year,path)
        return
    except:
        return


#Funktion Saldo zu erhöhen:
def increase_balance(amount, month, year, path):
    name = str(month) + str(year)
    data = load_json(path)
    balance = float(data[name]["balance"]) + float(amount)
    data[name]["balance"] = str(balance)
    save_json(path, data)
    return



#Funktion Saldo verringern
def decrease_balance(amount, month, year, path):
    name = str(month) + str(year)
    data = load_json(path)
    balance = float(data[name]["balance"]) - float(amount)
    data[name]["balance"] = str(balance)
    save_json(path, data)
    return



#Funktion um Monat zu löschen:
def month_delete(path,month,year):
    try:
        key = str(month) + str(year)
        data = load_json(path)
        data.pop(str(key))
        save_json(path,data)
        return
    except:
        return

