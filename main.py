from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect

app = Flask("time_recording")

#Home-Seite
@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

#Add-Seite
@app.route('/add')
def add():
	return render_template("add.html")

#Edit_main-Seite
@app.route('/edit')
def edit_main():
	return render_template("edit_main.html")

#Edit_fixkosten-Seite
@app.route('/edit/fixkosten')
def edit_fixkosten():
	return render_template("edit_fixkosten.html")

#Edit_fixeinnahmen-Seite
@app.route('/edit/fixeinnahmen')
def edit_fixeinnahmen():
	return render_template("edit_fixeinnahmen.html")

#Edit_monat_auswahl-Seite
@app.route('/edit/monat_auswahl')
def edit_monat_auswahl():
	return render_template("edit_monat_auswahl.html")

#Overview-Seite
@app.route('/overview')
def overview():
	return render_template("overview.html")

if __name__ == "__main__":
	app.run(debug=True, port=5000)