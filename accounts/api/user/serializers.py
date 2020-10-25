from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from django.utils import timezone
import datetime
from status.api.serializers import StatusInlineUserSerializer
# from .utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()


class UserDetailSerilaizer(serializers.ModelSerializer):
	uri = serializers.SerializerMethodField(read_only=True)
	status = serializers.SerializerMethodField(read_only=True)
	# status_uri = serializers.SerializerMethodField(read_only=True)
	# recent_status_list = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = User
		fields = [
		"id",
		"username",
		"uri",
		# "status_uri",
		# "recent_status_list",
		"status",
		]
	def get_uri(self, obj):
		return "/api/users/{id}/".format(id=obj.id)

	def get_status(self, obj):
		data = {
			"uri":self.get_uri(obj) + "status/",
			"last":self.get_last_status(obj),
			"recent":self.get_recent_status_list(obj),
		}
		return data	
	
	def get_recent_status_list(self, obj):
		qs = obj.status_set.all().order_by("-timestamp")[:5]# Status.objects.all(user=object)
		return StatusInlineUserSerializer(qs, many=True).data

	def get_last_status(self, obj):
		qs = obj.status_set.all().order_by("-timestamp")# Status.objects.all(user=object)
		return StatusInlineUserSerializer(qs.first()).data	