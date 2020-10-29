from rest_framework.test import APITestCase 

# Create your tests here.
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from django.urls import reverse
from rest_framework import status

User = get_user_model()

class UserAPITestCase(APITestCase):
	def setUp(self):
		user = User.objects.create(username="abhi", email="abhi@gmail.com")
		user.set_password("admin")
		user.save()

	def test_created_user_std(self):
		qs = User.objects.filter(username="abhi")
		self.assertEqual(qs.count(), 1)

	def test_register_user_api_fail(self):
		url = api_reverse("api-auth:register")
		data = {
		"username":"abhi1",
		"email":"abhi1@gmail.com",
		"password":"admin",
		}

		respose = self.client.post(url, data, format='json')
		# print(respose.data)
		# print(respose.status_code)
		self.assertEqual(respose.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(respose.data["password2"][0], "This field is required." )

	def test_register_user_api(self):
			url = api_reverse("api-auth:register")
			data = {
			"username":"abhi1",
			"email":"abhi1@gmail.com",
			"password":"admin",
			"password2":"admin",
			}

			respose = self.client.post(url, data, format='json')
			# print(respose.data)
			# print(respose.status_code)
			self.assertEqual(respose.status_code, status.HTTP_201_CREATED)
			token_len = len(respose.data.get("token", 0))
			self.assertGreater(token_len, 0)



	def test_login_user_api(self):
			url = api_reverse("api-auth:login")
			data = {
			"username":"abhi",
			"password":"admin",
			}

			respose = self.client.post(url, data, format='json')
			# print(respose.data)
			# print(respose.status_code)
			self.assertEqual(respose.status_code, status.HTTP_200_OK)
			token = respose.data.get("token", 0)
			token_len = 0
			if token != 0:
				token_len = len(token)
			self.assertGreater(token_len, 0)


	def test_login_user_api_fail(self):
			url = api_reverse("api-auth:login")
			data = {
			"username":"abhi",
			"password":"admin2", # wrong password
			}

			respose = self.client.post(url, data, format='json')
			# print(respose.data)
			# print(respose.status_code)
			self.assertEqual(respose.status_code, status.HTTP_401_UNAUTHORIZED)
			token = respose.data.get("token",0)
			token_len = 0 
			if token!=0:
				token_len = len(token)
			self.assertEqual(token_len, 0)		
	
	def test_token_login_api(self):
		url = api_reverse("api-auth:login")
		data = {
		"username":"abhi",
		"password":"admin",
		}
		respose = self.client.post(url, data, format='json')
		self.assertEqual(respose.status_code, status.HTTP_200_OK)
		token = respose.data.get("token", None)
		self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)
		response2 = self.client.post(url, data, format='json')
		self.assertEqual(respose.status_code, status.HTTP_200_OK)



