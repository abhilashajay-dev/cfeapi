import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from django.core.serializers import serialize 

# Create your views here.
from .models import Update

def json_example_view(request):
	data = {
	"count":4000
	}
	# URI -> REST API
	# GET REQUEST
	return JsonResponse(data) # return json data


class JSONCBV(View):
	def get(self, request, **kwargs):
		data = {
			"count":5000
			}
		return JsonResponse(data)		




class JSONCBV2(JsonResponseMixin, View):
	def get(self, context, *args, **kwargs):
		data = {
			"count":6000
			}
		return self.render_to_json_response(data)

# class SerializedDetailView( View):
# 	def get(self, context, *args, **kwargs):
# 		obj = Update.objects.get(id=1)
# 		data = {
# 			"user":obj.user.username,
# 			"content":obj.content,
# 			}
# 		json_data = json.dumps(data)	
# 		return HttpResponse(json_data, content_type="application/json")



class SerializedDetailView( View):
	def get(self, context, *args, **kwargs):
		obj = Update.objects.get(id=1)
		
		json_data = obj.serialize()	
		return HttpResponse(json_data, content_type="application/json")


class SerializedListView(View):
	def get(self, context, *args, **kwargs):
		# qs = Update.objects.all()
		# json_data = serialize("json", qs , fields=("user", "content"))	
		json_data = Update.objects.all().serialize()
		return HttpResponse(json_data, content_type="application/json")
