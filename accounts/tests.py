from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
	def setUp(self):
		user = User.objects.create(username="abhi", email="abhi@gmail.com")
		user.set_password("admin")
		user.save()

	def test_created_user(self):
		qs = User.objects.filter(username="abhi")
		self.assertEqual(qs.count(), 1)	