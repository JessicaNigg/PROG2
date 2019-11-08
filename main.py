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

#Edit_choose-Seite
@app.route('/edit')
def edit_choose():
	return render_template("edit_choose.html")

#Edit_month-Seite
@app.route('/edit/month')
def edit_month():
	return render_template("edit_month.html")

#Overview-Seite
@app.route('/overview')
def overview():
	return render_template("overview.html")

if __name__ == "__main__":
	app.run(debug=True, port=5000)