import requests
import json
import os 

meetup_api_key = os.environ['MEETUP_API_KEY']

def search_meetups(zip, radius):
	"""Creates an API call to the Meetups API"""
	
	url = 'https://api.meetup.com/2/open_events'
	myparams = {'key': meetup_api_key, 'sign': 'true', 'zip': zip, 'radius': radius, 'topic': 'python'}	
	response = requests.get(url, params = myparams)			# create API request the given parameters
	response_obj = response.text							# returns the text of the server's response 
	meetup_dict = json.loads(response_obj)					# takes a JSON string & turns it into a Python dict
	return meetup_dict

# test = search_meetups('94901', '15.0')
# test2 = test['results']
# print test2