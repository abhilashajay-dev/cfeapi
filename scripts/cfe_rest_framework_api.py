import requests
import json




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


# do(data={"id":37})	

# do(method='delete' ,data={"id":37})


do(method='put', data={"id":35 , "content":"Some new content", "user":1 })