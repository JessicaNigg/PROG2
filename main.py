from flask import Flask
from flask import render_template

app = Flask("time_recording")


if __name__ == "__main__":
	app.run(debug=True, port=5000)