from flask import Flask, render_template, redirect, request, flash, g, session as flask_session
import os

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']

@app.route("/")
def display_form():
	return render_template("index.html")

@app.route("/get_meetups")
def get_form_info():
	zipcode = request.args.get("zipcode")
	radius = ""

	return render_template("index.html")



if __name__ == "__main__":
	app.run(debug=True)