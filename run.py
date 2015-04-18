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
	radius = request.args.get("radius")
	#returns the number of days, weeks, months
	num_of_day_week_month = request.args.get("number")
	#returns a string "day(s)" "month(s)" "year(s)"
	days_week_month = request.args.get("timeframe")

	print zipcode
	print radius
	print num_of_day_week_month
	print days_week_month

	return "hi"



if __name__ == "__main__":
	app.run(debug=True)