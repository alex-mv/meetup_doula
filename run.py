from flask import Flask, render_template, redirect, request, flash, g, session as flask_session
import os
import requests
import json
import meetupapi
from pprint import pprint

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
meetup_api_key = os.environ['MEETUP_API_KEY']

@app.route("/")
def display_form():
    return render_template("index.html")

def is_for_beginner(text, word_list):
    """ utility function to help filter api response results for beginners"""
    for word in word_list:
        if word in text:
            return True
        return False

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

    meetup_results_dict = meetupapi.search_meetups(zipcode, radius)
    # print "meetup_results_dict BEFORE filter"
    # pprint(meetup_results_dict)

    # list of words to use in filtering for beginner results
    word_keys = ["intro ", "study group", "workshop", "fundamentals", "learn", "tutorial", "beginner"]

    for event in meetup_results_dict['results']:
        if 'description' in event.keys():
            text_to_search = event['description']
            if not is_for_beginner(text_to_search, word_keys):
                meetup_results_dict['results'].remove(event)
    # print "*"*13
    # print "meetup_results_dict AFTER filter"
    # pprint(meetup_results_dict)


    # renaming new dict to match name template is seeking
    meetup_dict = meetup_results_dict

    # print meetup_dict
    return render_template("display.html", events_dict = meetup_dict)

if __name__ == "__main__":
    app.run(debug=True)