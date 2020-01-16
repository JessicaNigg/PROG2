"""
Summary:
Libary of functions to edit, read and save data in files. 
"""

import json
import random


#function to save a json-file
def save_json(path, data):

    """
    Summary: 
    Creates a json file
    
    Args:
        path (dictionary): path and filename of the json file. 
        data (dict): content of json file  
    """

    with open(path, "w", encoding="utf-8") as open_file:
        json.dump(data, open_file, indent=4)

#function to load a json-file
def load_json(path):

    """
    Summary: 
    Gets the contents of a json file.
    
    Args:
        path (string): path of the json file
        
    Returns:
        dict : content of the json file
    """

    try:
        with open (path) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        data = {}
        return data

#function to save a month
def month_save(month, year, path):

    """
    Summary: 
    Saves a month with the inputs from the form.
    
    Args:
        path (string): path of the json file
        month (integer): month from the form
        year (integer): year from the form
    """

    #try to read json-file
    name = str(month) + str(year)
    data = load_json(path)
    if name in data:
        return
    else:
        data[name] = {
            "expenses": {}, "income":{}, "balance": "0"
        }
    save_json(path,data)


#function to edit a month
def expenses_update(path,key,month,year,amount,title):

    """
    Summary: 
    Edits a specific expense.
    
    Args:
        path (string): path of the json file
        key (string): key to identify the expense
        month (integer): month from the form
        year (integer): year from the form
        amount (integer): amount from the form
        title (string): title from the form
    """

    expenses_delete(path,key,month,year)
    expenses_add(month,year,amount,title,path)

def earnings_update(path,key,month,year,amount,title):

    """
    Summary: 
    Edits a specific earning.
    
    Args:
        path (string): path of the json file
        key (string): key to identify the earning
        month (integer): month from the form
        year (integer): year from the form
        amount (integer): amount from the form
        title (string): title from the form
    """

    earnings_delete(path,key,month,year)
    earnings_add(month,year,amount,title,path)

#function to add expenses
def expenses_add(month,year,amount,title,path):

    """
    Summary: 
    Adds expense to a month and calculates the sum.
    
    Args:
        month (integer): month from the form
        year (integer): year from the form
        amount (integer): amount from the form
        title (string): title from the form
        path (string): path of the json file
    """

    name = str(month) + str(year)
    key = int(name + str(random.randrange(0, 1000)))
    

    data = load_json(path)
    data[name]["expenses"][key] = { 'amount': str(amount), 'title': str(title)}
    
    save_json(path, data)
    decrease_balance(amount,month,year,path)


#function to delete expenses
def expenses_delete(path,key,month,year):

    """
    Summary: 
    Deletes expense from a month and calculates the sum.
    
    Args:
        path (string): path of the json file
        key (string): key to identify the expense
        month (integer): month from the form
        year (integer): year from the form
    """

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


#function to add earnings
def earnings_add(month,year,amount,title,path):

    """
    Summary: 
    Adds earning to a month and calculates the sum.
    
    Args:
        month (integer): month from the form
        year (integer): year from the form
        amount (integer): amount from the form
        title (string): title from the form
        path (string): path of the json file
    """

    name = str(month) + str(year)
    key = int(name + str(random.randrange(0, 1000)))

    data = load_json(path)
    if name not in data:
        month_save(month, year, path)
        data = load_json(path)
    
    data[name]["income"][key] = { 'amount': str(amount), 'title': str(title)}
    
    save_json(path, data)

    increase_balance(amount,month,year,path)



#function to delete earnings
def earnings_delete(path,key,month,year):

    """
    Summary: 
    Deletes earning from a month and calculates the sum.
    
    Args:
        path (string): path of the json file
        key (string): key to identify the earning
        month (integer): month from the form
        year (integer): year from the form
    """

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


#function to increase the balance
def increase_balance(amount, month, year, path):

    """
    Summary: 
    Increases the sum from a month by the specified amount.
    
    Args:
        amount (integer): amount from the form
        month (integer): month from the form
        year (integer): year from the form
        path (string): path of the json file
    """

    name = str(month) + str(year)
    data = load_json(path)
    balance = float(data[name]["balance"]) + float(amount)
    data[name]["balance"] = str(balance)
    save_json(path, data)



#function to decrease the balance
def decrease_balance(amount, month, year, path):

    """
    Summary: 
    Decreases the sum from a month by the specified amount.
    
    Args:
        amount (integer): amount from the form
        month (integer): month from the form
        year (integer): year from the form
        path (string): path of the json file
    """

    name = str(month) + str(year)
    data = load_json(path)
    balance = float(data[name]["balance"]) - float(amount)
    data[name]["balance"] = str(balance)
    save_json(path, data)



#function to delete a month
def month_delete(path,month,year):

    """
    Summary: 
    Deletes the specified month.
    
    Args:
        path (string): path of the json file
        month (integer): month from the form
        year (integer): year from the form
    """

    try:
        key = str(month) + str(year)
        data = load_json(path)
        data.pop(str(key))
        save_json(path,data)
        return
    except:
        return

