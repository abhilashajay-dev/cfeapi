from six import BytesIO #-----> install pip six & pip install --upgrade django-cors-headers
# from django.utils.six import BytesIO ---> this was removed from django 3.0 refer to -->https://stackoverflow.com/questions/59193514/importerror-cannot-import-name-six-from-django-utils
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from status.models import Status
from status.api.serializers import StatusSerializer

# Serialize a single object

obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data

	"""Converting Serialized data into JSON"""
json_data = JSONRenderer().render(serializer.data)
print(json_data)
print(type(json_data))
		
		""" conversion of JSON ---> List object """
stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)
type(data)


# Serialize a queryset 

qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)
print(type(json_data2))

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)
type(data2)


# Create object
data = {'user':1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()


# Update object
obj = Status.objects.first()

data = {"content":"update from serializer", "user":1}

update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()




# Delete object

data = {"content":"DELETE ME", "user":1}

delete_obj = StatusSerializer(data=data)
delete_obj.is_valid()
delete_obj.save()

obj_delete_last = Status.objects.last()

print(obj_delete_last) 


# CustomSerializer
from rest_framework import serializers


class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()



data ={'email':"hello@gmail.com", "content":"from custom serializer"}
CS_serializer =	 CustomSerializer(data=data)
CS_serializer.is_valid()
CS_serializer.save()
