
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse


# A single end point for creating ,retrieving, updating and deleting (1)UpdateModel
class UpdateModelDetailAPIView(View):  # retrive , update, delete

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        return HttpResponse(json_data, content_type='application/json')


class UpdateModelListAPIView(View):  # list & create

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return HttpResponse(json_data, content_type='application/json')
