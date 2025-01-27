import requests
import json
import os


image_path = os.path.join(os.getcwd(), "img1.png")

ENDPOINT = "http://127.0.0.1:8000/api/status/"

# def do(method='get', data={}, id=41, is_json=True):
def do(method='get', data={}, is_json=True):
	headers = {}
	if is_json:
		headers['content-type']="application/json"
		data=json.dumps(data)		
	# r =requests.request(method, ENDPOINT + "?id=" +str(id), data=data)
	r =requests.request(method, ENDPOINT , data=data, headers=headers)
	print(r.text)
	return r


def do_img(method='get', data={}, is_json=True, img_path=None):
	headers = {}
	if is_json:
		headers['content-type']="application/json"
		data=json.dumps(data)		
	# r =requests.request(method, ENDPOINT + "?id=" +str(id), data=data)
	if img_path is not None:
		with open(image_path, 'rb') as image:
			file_data = {"image":image}	#----> since to match the field in serializer
			r =requests.request(method, ENDPOINT , data=data, headers=headers, files=file_data)
	r =requests.request(method, ENDPOINT , data=data, headers=headers)
	print(r.text)
	return r	


# do(data={"id":37})	

# do(method='delete' ,data={"id":35})


# do(method='put', data={"id":35 , "content":"Some new content", "user":1 })


# do(method='post', data={ "content":"Some new content by post", "user":1 })

do_img(method='post', data={ "content":"Some new content by post", "user":1 }, is_json=False, img_path=image_path) #--->since image is derived from file 


