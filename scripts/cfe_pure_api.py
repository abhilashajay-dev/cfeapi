import requests
import json


BASE_URL = " http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    for obj in data:
    	if obj['id']==2:
	    	r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
	    	print(f'Object called using Object ID :',r2.json(),'\n')
	    	# data = r2.json()
	    	# print(dir(r2))
    return data


def create_update():
	new_data= {
	'user':1,
	'content':""
	}

	r = requests.post(BASE_URL + ENDPOINT, data=new_data)
	print(r.headers)
	if r.status_code == requests.codes.ok : 
		print(r.json())
		return r.json()
	return r.text    
    	
# print(get_list())
print(create_update())