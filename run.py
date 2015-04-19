from flask import Flask, render_template, redirect, request, flash, g, session as flask_session
import os
import requests
import json
import meetupapi

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
meetup_api_key = os.environ['MEETUP_API_KEY']

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

	# print zipcode
	# print radius
	# print num_of_day_week_month
	# print days_week_month

	# test api call with hard coded values
	# meetup_dict = meetupapi.search_meetups('94901', '15.0')

	meetup_dict = meetupapi.search_meetups(zipcode, radius)
	# print meetup_dict
	print meetup_dict
	return render_template("display.html", events_dict = meetup_dict)

if __name__ == "__main__":
	app.run(debug=True)