import requests
import json
import os

image_path = os.path.join(os.getcwd(), "img1.png")

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTHENDPOINT = "http://127.0.0.1:8000/api/auth/"#-----> changend according to url of the view
REFRESHENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/refresh/"
REGISTERENDPOINT ="http://127.0.0.1:8000/api/auth/register/"

get_endpoint = ENDPOINT + str(48) 

post_data = json.dumps({"content":"Some random content"})

# get request test
# r = requests.get(get_endpoint)

# print(r.text)
# print(r.status_code)

post_headers = {"content-type":"application/json",
# "Authorization":"JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNSwidXNlcm5hbWUiOiJhZG1pbjEiLCJleHAiOjE2MDI5Nzc0NjQsImVtYWlsIjoiYWRtaW4xQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNjAyOTc3MTY0fQ.JzM_KgMG52-JTlKMsc9MqpY-ExDGc8GtiXjvB1hPhGc'
}

# token authentication

auth_data = {
	"username":'admin16',
	"email":"admin16@gmail.com",
	"password":'admin',
	"password2":'admin',
}


r3  = requests.post(REGISTERENDPOINT, data=json.dumps(auth_data), headers=post_headers)
token   =  r3.json()
print(token)