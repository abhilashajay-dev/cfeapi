import requests
import json
import os

image_path = os.path.join(os.getcwd(), "img1.png")

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTHENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
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


# # Refresh Tokens 
refresh_data = {"token":token}
r4  = requests.post(REFRESHENDPOINT, data=json.dumps(refresh_data), headers=post_headers)
new_token   =  r4.json()["token"]
print(new_token)

# Token are not same
if token == new_token:
	print("true")
else:
	print("not same")


# post request for image test



headers = {
# "content-type":"application/json",
"Authorization":"JWT " + token,
}

with open(image_path, 'rb') as image:
	file_data = {'image':image}	

	data ={'content':"image content using Jwt pure cfe api test"}

	posted_response = requests.post(ENDPOINT, data=data, headers=headers, files=file_data)

	print(posted_response.text)
	print(posted_response.status_code)