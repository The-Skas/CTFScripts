
#Hello ICTF
import json
import requests
import pdb
import sys

#Test URL
# url = 'http://maps.googleapis.com/maps/api/directions/json'

url = sys.argv[1]
params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

def test_json():
	r = requests.get(url, params=params)
	js = r.json()
	recursive_json_print(js, "   ")



def recursive_json_print(my_json, str_padding = " ", rec_depth = 0):
	"""
	This may seem quite complicated for a JSON print and it probably is.
	This is due to me testing on recursive json data which could be lists, 
	or dictionaries. 
	"""
	for key, value in my_json.iteritems():
		print str_padding*rec_depth,str(key)+": ",

		if type(value) == type(['']):
			for sub_value in value:
				print ""
				#The values sometimes are just zero
				if type(sub_value) == dict: 
					recursive_json_print(sub_value, str_padding, rec_depth + 1)
				else:
					print (str_padding*rec_depth),sub_value
		elif type(value) == dict:
			print ""
			recursive_json_print(value, str_padding, rec_depth + 1)
		else:
			print str_padding*rec_depth, value

test_json()

# all_services = get_service_list()

# for service in all_services:
# 	#This gets all the targets running a particular service.

# 	#TODO: Might need to pass 'service.id' or 'service.name' instead
# 	targets_with_service =  get_targets(service)