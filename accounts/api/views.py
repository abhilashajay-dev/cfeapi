from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model


class AuthView(APIView):
	authentication_classes = []
	permission_classes = [permissions.AllowAny]
	def post(self, request, *args, **kwargs):
		print(request.user)
		if request.user.is_authenticated:
			return Response({"detail":"You are already authenticated"}, status=400)
		data = request.data
		username = data.get('username')
		password = data.get('password')
		user = authenticate(username=username, password=password)
		print(user)
		return Response({'token':'abc'})

