from django.http import JsonResponse, HttpResponse



class JsonResponseMixin(object):
	def render_to_json_response(self, context, **response_kwargs):
		return JsonResponse(self.get_data(context), **response_kwargs)

	def get_data(self, context):
		return context	


class HttpResponseMixin(object):
	is_json = False
	def render_to_response(self, json_data, status=200):
		content_type = 'text/html'
		if self.is_json:
			content_type = 'application/json'
		return HttpResponse(json_data, content_type= content_type, status=status)