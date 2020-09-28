# from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404



# class StatusListSearchAPIView(APIView):
# 	permission_classes = [ ]
# 	authentication_classes = []

# 	def get(self, request, format=None):
# 		qs = Status.objects.all()
# 		serializer = StatusSerializer(qs, many=True)
# 		return Response(serializer.data)


class StatusAPIView(
	mixins.CreateModelMixin,
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
 	generics.ListAPIView): #-----> CRUD in a single endpoint
	permission_classes = []
	authentication_classes = []
	queryset = Status.objects.all()
	serializer_class = StatusSerializer

	def get_queryset(self):
		qs = Status.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(content__icontains=query)
		return qs 

	def  get_object(self):
		passed_id = self.request.GET.get('id', None)
		queryset = self.get_queryset()
		obj = None
		if passed_id is not None:
			obj = get_object_or_404(queryset, id=passed_id)
			self.check_object_permissions(self.request, obj) #-----> rest_framework method
		return obj 

	def get(self, request, *args, **kwargs):
		passed_id =  request.GET.get('id', None)
		if passed_id is not None:
			return self.retrieve(request, *args, **kwargs) #---->RetrieveModelMixin method overides get_object()
		return super().get(request ,*args, **kwargs)	#----> overriding the inbuilt get method of ListAPIView	


	
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)#---->CreateModelMixin method .create(request, *args, **kwargs)			

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)		

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


# class StatusCreateAPIView(generics.CreateAPIView):
# 	permission_classes = []
# 	authentication_classes = []
# 	queryset = Status.objects.all()
# 	serializer_class = StatusSerializer

# 	# def perform_create(self, serializer):
# 	# 	serializer.save(user=self.request.user)

# class StatusDetailAPIView(mixins.DestroyModelMixin ,mixins.UpdateModelMixin ,generics.RetrieveAPIView):
# 	permission_classes = []
# 	authentication_classes = []
# 	queryset = Status.objects.all()
# 	serializer_class = StatusSerializer
# 	lookup_field = 'id' #'slug'

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)
	
# 	def patch(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)		

# 	# def get_object(self, *args, **kwargs):
# 	# 	kwargs = self.kwargs
# 	# 	kw_id = kwargs.get('id')
# 	# 	return Status.objects.get(id=kw_id)

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
