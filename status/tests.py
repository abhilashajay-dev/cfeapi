from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Status

User = get_user_model()

class StatusTestCase(TestCase):
	def setUp(self):
		user = User.objects.create(username="abhi", email="abhi@gmail.com")
		user.set_password("admin")
		user.save()

	def test_creating_status(self):
		user = User.objects.get(username="abhi")
		obj = Status.objects.create(user=user, content="test content")
		self.assertEqual(obj.id, 1)
		qs = Status.objects.all()
		self.assertEqual(qs.count(), 1)	