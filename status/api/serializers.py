from rest_framework import serializers
from status.models import Status




# Serializers can turn data into JSON and also Validate data similar to forms
class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ["user", "content", "image", "id"]

		read_only_fields = ["user"]

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


