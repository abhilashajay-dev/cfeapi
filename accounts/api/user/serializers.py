from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from django.utils import timezone
import datetime
# from .utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()


class UserDetailSerilaizer(serializers.ModelSerializer):
	uri = serializers.SerializerMethodField(read_only=True)
	status_list = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = User
		fields = [
		"id",
		"username",
		"uri",
		"status_list",
		]
	def get_uri(self, obj):
		return "/api/users/{id}/".format(id=obj.id)
	
	def get_status_list(self, obj):
		pass