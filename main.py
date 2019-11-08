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

#Month_overview-Seite
@app.route('/month_overview')
def month_overview():
	return render_template("month_overview.html")

#Month_edit-Seite
@app.route('/month_edit')
def month_edit():
	return render_template("month_edit.html")

if __name__ == "__main__":
	app.run(debug=True, port=5000)