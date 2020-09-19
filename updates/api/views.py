
import json
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from .mixins import CSRFExemptMixin
from cfeapi.mixins import HttpResponseMixin

# A single end point for creating ,retrieving, updating and deleting (1)UpdateModel
class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):  # retrive , update, delete

    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data={}
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data={}
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_response(json_data)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):  # list & create


    # def render_to_response(json_data, status=200):  --> added the same function in mixin 
    #     return HttpResponse(json_data, content_type='application/json', status=status)

    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message":"unkown data"})
        # return HttpResponse(json_data, content_type='application/json', status=400)
        return self.render_to_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps( {"message":"you cannot delete an entire list"})
        status_code = 403 #Forbidden
        # return HttpResponse(json_data, content_type='application/json', status=status_code)
        return self.render_to_response(json_data, status=status_code)