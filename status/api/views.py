# from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializer



class StatusListSearchAPIView(APIView):
	permission_classes = []
	authentication_classe = []

	def get(self, request, format=None):
		qs = Status.objects.all()
		serializer = StatusSerializer(qs, many=True)
		return Response(serializer.data)


class StatusAPIView(generics.ListAPIView):
	permission_classes = []
	authentication_classe = []
	queryset = Status.objects.all()
	serializer_class = StatusSerializer