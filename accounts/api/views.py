from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings
# from .utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()

class AuthView(APIView):
	authentication_classes = []
	permission_classes = [permissions.AllowAny]
	def post(self, request, *args, **kwargs):
		print(request.user)
		if request.user.is_authenticated:
			return Response({"detail":"You are already authenticated"}, status=400)
		data = request.data
		username = data.get('username') # username or email
		password = data.get('password')
		# user = authenticate(username=username, password=password)
		qs = User.objects.filter(
				Q(username__iexact=username)|
				Q(email__iexact=username)
			).distinct()
		if qs.count() == 1:
			user_obj = qs.first()
			if user_obj.check_password(password):
				user = user_obj	
				print(user)
				payload = jwt_payload_handler(user)
				token = jwt_encode_handler(payload)
				response = jwt_response_payload_handler(token, user, request=request)
				return Response(response)
		return Response({"detail": "invalid credentials"}, status=401)	

class RegisterAPIView(APIView):
	authentication_classes = []
	permission_classes = [permissions.AllowAny]
	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return Response({"detail":"you are already registered"})
		data = request.data
		username = data.get("username")
		password = data.get("password")
		password2 = data.get("password2")
		#Validatind username and password and email
		qs = User.objects.filter(Q(username__iexact=username)|Q(email__iexact=username))
		if qs.exists():
			return Response({"detail":"username already exists"}, status=400)
		if 	password != password2:
			return Response({"detail":"password must be same"})
		else:
			user = User.objects.create(username=username, email=username) # ---> since some prefer email as username	
			user.set_password(password)
			user.save()
			print(user)
			payload = jwt_payload_handler(user)
			token = jwt_encode_handler(payload)
			response = jwt_response_payload_handler(token, user, request=request)
			return Response(response)
		return Response({"detail": "invalid requests"}, status=401)	

