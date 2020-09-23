
import json
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from .mixins import CSRFExemptMixin
from cfeapi.mixins import HttpResponseMixin
from updates.forms import UpdateModelForm
from .utils import is_json

# A single end point for creating ,retrieving, updating and deleting (1)UpdateModel
class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):  # retrive , update, delete

    is_json = True

    def get_obj(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None    


    def get(self, request, id, *args, **kwargs):

        obj = self.get_obj(id=id)
        if obj.id is None:
            error_data = json.dumps({'message':'Update not found'})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_response(json_data)

    def put(self, request, id, *args, **kwargs):
        obj = self.get_obj(id=id)
        if obj.id is None:
            error_data = json.dumps({'message':'Update not found'})
            return self.render_to_response(error_data, status=404)
        # return HttpResponse(json_data, content_type='application/json')
        # print(dir(request))
        print(request.body)
        valid_json=is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message':'Invalid data sent please send using JSON'})
            return self.render_to_response(error_data, status=400)

        new_data = json.loads(request.body)
        print(new_data['content'])
        json_data = json.dumps({'message':'Something is new'})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_obj(id=id)
        if obj.id is None:
            error_data = json.dumps({'message':'Update not found'})
            return self.render_to_response(error_data, status=404)
        # json_data = obj.serialize()
        json_data=json.dumps({'message':"something"})
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
        valid_json=is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message':'Invalid data sent please send using JSON'})
            return self.render_to_response(error_data, status=400)

        new_data = json.loads(request.body)
        
        form = UpdateModelForm(new_data or None)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data , status=400)     

        json_data = json.dumps({"message":"unkown data"})
        print(request.POST)
        # return HttpResponse(json_data, content_type='application/json', status=400)
        return self.render_to_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps( {"message":"you cannot delete an entire list"})
        status_code = 403 #Forbidden
        # return HttpResponse(json_data, content_type='application/json', status=status_code)
        return self.render_to_response(json_data, status=status_code)