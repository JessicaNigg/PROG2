from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect

app = Flask("time_recording")

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True, port=5000)