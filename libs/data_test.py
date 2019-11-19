import json

#Funktion um einen Monat zu speichern:
def month_save(month, year):
    #Versuch Json auszulesen
    name = str(month) + str(year)
    try:
        with open ('data/data.json') as file:
            form_inputs = json.load(file)
    except FileNotFoundError:
        form_inputs = {}

    form_inputs[str(month)+str(year)] = {
            "ausgaben": [], "einnahmen": []
        }
    print(form_inputs)

month_save("05", "2019")


#Funktion um einen Monat zu bearbeiten:
def month_edit():



#Funktion um einen Monat in der Übersicht anzuzeigen:
def month_overview():



#Funktion um Kosten hinzuzufügen:
def cost_add():


#Funktion um Kosten zu löschen:
def cost_delete():


#Funktion um Einnahmen hinzuzufügen:
def earnings_add():


#Funktion um Einnahmen zu löschen:
def earnings_delete():


#Funktion um Einnahmen & Kosten eines Monats als Summe zu berechnen:
def calculate_month():


    