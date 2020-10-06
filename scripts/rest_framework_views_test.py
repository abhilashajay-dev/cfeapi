import requests
import json
import os

image_path = os.path.join(os.getcwd(), "img1.png")

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTHENDPOINT = "http://127.0.0.1:8000/api/auth/"#-----> changend according to url of the view
REFRESHENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/refresh/"

get_endpoint = ENDPOINT + str(48) 

post_data = json.dumps({"content":"Some random content"})

# get request test
r = requests.get(get_endpoint)

print(r.text)
print(r.status_code)

post_headers = {"content-type":"application/json"}

# token authentication

auth_data = {
	"username":'admin',
	"password":'admin',
}


r3  = requests.post(AUTHENDPOINT, data=json.dumps(auth_data), headers=post_headers)
token   =  r3.json()["token"] 
print(token)