import json
def add_month(month, year):
    name = str(month) + str(year) + ".json"
    data = {
            "ausgaben": [], "einnahmen": []
        }
    path = "data/" + name
    with open(path, "w", encoding="utf-8") as open_file:
        json.dump(data, open_file, indent=4)

add_month('01', 2019)