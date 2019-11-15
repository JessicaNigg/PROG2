from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

app = Flask("time_recording")

#Home-Seite
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	print(request.form)
	if request.method == 'POST':
		year = request.form['year']
		month = request.form['month']
		if request.form['submit'] == 'uebersicht':
			return redirect(url_for('month_overview', year = year, month = month))
		elif request.form['submit'] == 'bearbeiten':
			return redirect(url_for('month_edit', year = year, month = month))
		elif request.form['submit'] == 'hinzufuegen':
			return redirect(url_for('month_edit', year = year, month = month))

	return render_template("index.html")

#Add-Seite
@app.route('/add')
def add():
	return render_template("add.html")


#Month_overview-Seite
@app.route('/month_overview', methods=['GET', 'POST'])
@app.route('/month_overview/<year>/<month>', methods=['GET', 'POST'])
def month_overview(year=None, month=None):
	return render_template("month_overview.html")

#Month_edit-Seite
@app.route('/month_edit', methods=['GET', 'POST'])
@app.route('/month_edit/<year>/<month>', methods=['GET', 'POST'])
def month_edit(year=None, month=None):
	return render_template("month_edit.html")

if __name__ == "__main__":
	app.run(debug=True, port=5000)