from django.db.models import Q
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings
# from .serializers import UserRegisterSerializer
from .serializers import UserDetailSerilaizer
from accounts.api.permissions import AnonPermissionOnly
from status.api.serializers import StatusInlineUserSerializer
from status.models import Status

# from .utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
	serializer_class = UserDetailSerilaizer
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	queryset = User.objects.filter(is_active=True)
	lookup_field = "username" #instead of id


class UserStatusAPIView(generics.ListAPIView):
	serializer_class = StatusInlineUserSerializer

	def get_queryset(self, *args, **kwargs):
		username = self.kwargs.get("username", None)
		if username is None:
			return Status.objects.none()
		return Status.objects.filter(user__username=username)		