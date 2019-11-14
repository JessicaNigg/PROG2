from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

app = Flask("time_recording")

#Home-Seite
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	print(request.form)
	if request.method == 'POST':
		year = request.form['year']
		month = request.form['month']
		if request.form['submit'] == 'overview':
			return redirect(url_for('month_overview', year = year, month = month))
		elif request.form['submit'] == 'edit':
			return redirect(url_for('month_edit'))

	return render_template("index.html")

#Add-Seite
@app.route('/add')
def add():
	return render_template("add.html")

#Month_overview-Seite
@app.route('/month_overview')
@app.route('/month_overview/<year>/<month>')
def month_overview(year=None, month=None):
	return render_template("month_overview.html")

#Month_edit-Seite
@app.route('/month_edit')
def month_edit():
	return render_template("month_edit.html")

if __name__ == "__main__":
	app.run(debug=True, port=5000)