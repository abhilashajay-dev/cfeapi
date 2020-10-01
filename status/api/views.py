# from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.authentication  import SessionAuthentication 
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404
import json
from .utils import is_json

class StatusAPIView(
	mixins.CreateModelMixin,
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
 	generics.ListAPIView): #-----> CRUD in a single endpoint
	permission_classes = []
	authentication_classes = [SessionAuthentication,]
	queryset = Status.objects.all()
	serializer_class = StatusSerializer
	passed_id = None #-----> to avoid error 

	def get_queryset(self):
		qs = Status.objects.all()
		print(self.request.user)
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(content__icontains=query)
		return qs 

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)#---->CreateModelMixin method .create(request, *args, **kwargs)			

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
		# pass

# 	# def get_object(self, *args, **kwargs):
# 	# 	kwargs = self.kwargs
# 	# 	kw_id = kwargs.get('id')
# 	# 	return Status.objects.get(id=kw_id)

class StatusDetailAPIView(
	mixins.DestroyModelMixin, 
	mixins.UpdateModelMixin,
	generics.RetrieveAPIView):
	permission_classes = []
	authentication_classes = []
	queryset = Status.objects.all()
	serializer_class = StatusSerializer
	lookup_field = 'id' #'slug'

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
	
	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)		

	def perform_update(self, serializer):
		 # serializer.save(updated_by_user=self.request.user)
		 pass

	def perform_destroy(self, instance):
		# if instance is not None:
		# 	return instance.delete()
		# return None	
		pass


# class StatusListSearchAPIView(APIView):
# 	permission_classes = [ ]
# 	authentication_classes = []

# 	def get(self, request, format=None):
# 		qs = Status.objects.all()
# 		serializer = StatusSerializer(qs, many=True)
# 		return Response(serializer.data)


# class StatusAPIView(
# 	mixins.CreateModelMixin,
# 	mixins.RetrieveModelMixin,
# 	mixins.UpdateModelMixin,
# 	mixins.DestroyModelMixin,
#  	generics.ListAPIView): #-----> CRUD in a single endpoint
# 	permission_classes = []
# 	authentication_classes = []
# 	queryset = Status.objects.all()
# 	serializer_class = StatusSerializer
# 	passed_id = None #-----> to avoid error 

# 	def get_queryset(self):
# 		qs = Status.objects.all()
# 		query = self.request.GET.get('q')
# 		if query is not None:
# 			qs = qs.filter(content__icontains=query)
# 		return qs 

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)#---->CreateModelMixin method .create(request, *args, **kwargs)			
	

# 	def  get_object(self):
# 		passed_id = self.request.GET.get('id', None) or self.passed_id
# 		queryset = self.get_queryset()
# 		obj = None
# 		if passed_id is not None:
# 			obj = get_object_or_404(queryset, id=passed_id)
# 			self.check_object_permissions(self.request, obj) #-----> rest_framework method
# 		return obj 

# 	def get(self, request, *args, **kwargs):
# 		url_passed_id = request.GET.get('id', None)
# 		json_data = {} #---> have to initialized a python dict in order to convert the request.body to python dic and extract value of id
# 		body_ = request.body
# 		if is_json(body_):
# 			json_data = json.loads(request.body)
# 		new_passed_id = json_data.get('id', None)
# 		print(request.body)
# 		# print(request.data)
# 		passed_id = url_passed_id or new_passed_id or None
# 		self.passed_id = passed_id
# 		if passed_id is not None:
# 			return self.retrieve(request, *args, **kwargs) #---->RetrieveModelMixin method overides get_object()
# 		return super().get(request ,*args, **kwargs)	#----> overriding the inbuilt get method of ListAPIView	


	

# 	# def perform_create(self, serializer):
# 	# 	serializer.save(user=self.request.user)

# 	def put(self, request, *args, **kwargs):
# 		url_passed_id = request.GET.get('id', None)
# 		json_data = {} #---> have to initialized a python dict in order to convert the request.body to python dic and extract value of id
# 		body_ = request.body
# 		if is_json(body_):
# 			json_data = json.loads(request.body)
# 		new_passed_id = json_data.get('id', None)
# 		print(request.body)
# 		# print(request.data)
# 		passed_id = url_passed_id or new_passed_id or None
# 		self.passed_id = passed_id
# 		return self.update(request, *args, **kwargs)
	
# 	def patch(self, request, *args, **kwargs):
# 		url_passed_id = request.GET.get('id', None)
# 		json_data = {} #---> have to initialized a python dict in order to convert the request.body to python dic and extract value of id
# 		body_ = request.body
# 		if is_json(body_):
# 			json_data = json.loads(request.body)
# 		new_passed_id = json_data.get('id', None)
# 		print(request.body)
# 		# print(request.data)
# 		passed_id = url_passed_id or new_passed_id or None
# 		self.passed_id = passed_id
# 		return self.update(request, *args, **kwargs)		

# 	def delete(self, request, *args, **kwargs):
# 		url_passed_id = request.GET.get('id', None)
# 		json_data = {} #---> have to initialized a python dict in order to convert the request.body to python dic and extract value of id
# 		body_ = request.body
# 		if is_json(body_):
# 			json_data = json.loads(request.body)
# 		new_passed_id = json_data.get('id', None)
# 		print(request.body)
# 		# print(request.data)
# 		passed_id = url_passed_id or new_passed_id or None
# 		self.passed_id = passed_id    
# 		return self.destroy(request, *args, **kwargs)


# class StatusCreateAPIView(generics.CreateAPIView):
# 	permission_classes = []
# 	authentication_classes = []
# 	queryset = Status.objects.all()
# 	serializer_class = StatusSerializer

# 	# def perform_create(self, serializer):
# 	# 	serializer.save(user=self.request.user)


# class StatusUpdateAPIView(generics.UpdateAPIView):
# 	permission_classes = []
# 	authentication_classes = []
# 	queryset = Status.objects.all()
# 	serializer_class = StatusSerializer
# 	lookup_field = 'id' #'slug'


# class StatusDeleteAPIView(generics.DestroyAPIView):
# 	permission_classes = []
# 	authentication_classes = []
# 	queryset = Status.objects.all()
# 	serializer_class = StatusSerializer
# 	lookup_field = 'id' #'slug'
