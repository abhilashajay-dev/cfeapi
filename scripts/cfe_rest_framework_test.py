import requests
import json
import os

image_path = os.path.join(os.getcwd(), "img1.png")

ENDPOINT = "http://127.0.0.1:8000/api/status/"

get_endpoint = ENDPOINT + str(48) 

post_data = json.dumps({"content":"Some random content"})

#get request test
r = requests.get(get_endpoint)

print(r.text)
print(r.status_code)

post_headers = {"content-type":"application/json"}

# post request test
r2 = requests.post(ENDPOINT, data=post_data, headers=post_headers)

print(r2.text)
print(r2.status_code)