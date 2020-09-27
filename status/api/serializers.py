from rest_framework import serializers
from status.models import status


# Serializers can turn data into JSON and also Validate data similar to forms
class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ['user','content', 'image',]