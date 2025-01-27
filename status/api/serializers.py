from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserPublicSerilaizers
from rest_framework.reverse import reverse as api_reverse

class StatusInlineUserSerializer(serializers.ModelSerializer):
	uri = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Status
		fields = ["content", "image", "id", "uri"]

	# def get_uri(self, obj):
	# 	return "/api/status/{id}".format(id=obj.id)	

	def get_uri(self, obj):
		request = self.context.get('request')
		return api_reverse("api-status:detail", kwargs={"id":obj.id}, request=request)
	




# Serializers can turn data into JSON and also Validate data similar to forms
class StatusSerializer(serializers.ModelSerializer):
	user  = UserPublicSerilaizers(read_only=True)
	uri = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Status
		fields = ["user", "content", "image", "id", "uri"]

		read_only_fields = ["user"]

	def get_uri(self, obj):
		request = self.context.get('request')
		return api_reverse("api-status:detail", kwargs={"id":obj.id}, request=request)
		

	# def get_uri(self, obj):
	# 	return "/api/status/{id}".format(id=obj.id)	

	# def validate_<fieldname>(self, value):
	# 	return	

	# def validate_content(self,value):
	# 	if len(value) > 240:
	# 		raise serializers.ValidationError("Content is too long")
	# 	return value	

	def validate(self, data):
	        content = data.get('content', None)
	        if content == "":
	            content = None
	        image = data.get('image', None)
	        if content is None and image is None:
	            raise serializers.ValidationError("image or content is required")
	        return data


