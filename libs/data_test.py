import json

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


    