from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from libs import data_helper

app = Flask("time_recording")

path = "./data/data.json"

# Home-Seite
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit'] == 'uebersicht':
            year = request.form['year']
            month = request.form['month']
            data = data_helper.load_json(path)
            name = str(month) + str(year)
            data = data_helper.load_json(path)
            if name in data:
                income = data[name]["income"]
                balance = data[name]["balance"]
                expenses = data[name]["expenses"]
                return render_template("month_overview.html", expenses=expenses, income=income, balance=balance, year=year, month=month)
            else:
                return redirect((url_for("index")))
        elif request.form['submit'] == 'hinzufuegen':
            year = request.form['year']
            month = request.form['month']
            data_helper.month_save(month, year, path)
            return render_template("index.html")
        elif request.form['submit'] == 'loeschen':
            year = request.form['year']
            month = request.form['month']
            data = data_helper.load_json(path)
            name = str(month) + str(year)
            if name in data:
                data_helper.month_delete(path,month,year)
            else:
                return render_template("index.html")
        elif request.form['submit'] == 'hinzufuegen_earning':
            year = request.form['year']
            month = request.form['month']
            amount = request.form['amount']
            title = request.form['title']
            data_helper.earnings_add(month, year, amount, title, path)
            return render_template("index.html")
        elif request.form['submit'] == 'hinzufuegen_expenses':
            year = request.form['year']
            month = request.form['month']
            amount = request.form['amount']
            title = request.form['title']
            data_helper.expenses_add(month, year, amount, title, path)
            return render_template("index.html")

    return render_template("index.html")


# Month_overview-Seite

@app.route('/delete/earning/<key>/<year>/<month>')
def delete_earning(key, year, month):
    data_helper.earnings_delete(path, key, month, year)
    return redirect((url_for("index")))


@app.route('/delete/expenses/<key>/<year>/<month>')
def delete_expenses(key, year, month):
    data_helper.expenses_delete(path, key, month, year)
    return redirect((url_for("index")))


@app.route('/edit/expenses/<key>/<year>/<month>', methods=['GET', 'POST'])
def edit_expenses(key, year, month):
    if request.method == 'POST':
        amount = request.form['amount']
        title = request.form['title']
        data_helper.expenses_update(path, key, month, year, amount, title)
        return redirect((url_for("index")))
    data = data_helper.load_json(path)
    name = str(month) + str(year)
    amount = data[name]["expenses"][key]["amount"]
    title = data[name]["expenses"][key]["title"]
    return render_template("edit_amount.html", key=key, month=month, year=year, amount=amount, title=title)


@app.route('/edit/earning/<key>/<year>/<month>', methods=['GET', 'POST'])
def edit_earnings(key, year, month):
    if request.method == 'POST':
        amount = request.form['amount']
        title = request.form['title']
        data_helper.earnings_update(path, key, month, year, amount, title)
        return redirect((url_for("index")))
    data = data_helper.load_json(path)
    name = str(month) + str(year)
    amount = data[name]["income"][key]["amount"]
    title = data[name]["income"][key]["title"]
    return render_template("edit_amount.html", key=key, month=month, year=year, amount=amount, title=title)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
