from django.db import models
from django.conf import settings 
from django.core.serializers import serialize
import json 

def upload_update_image(instance, filename):
	return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class UpdateQuerySet(models.QuerySet):
	# def serialize(self):
	# 	qs = self
	# 	return serialize('json', qs, fields=('user', 'content', 'image'))

	def serialize(self): # this is for making output as a list of json ---> making it cleaner than serialized data
		list_values = list(self.values('user','content','image'))
		return json.dumps(list_values)
	


class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self._db)		



# Create your models here.
class Update(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(blank=True,null=True)
	image = models.ImageField(upload_to=upload_update_image,blank=True, null=True )
	timestamp = models.TimeField(auto_now_add=True)
	updated = models.TimeField(auto_now=True)
	objects = UpdateManager()

	def __str__(self):
		return self.content or ""

	# def serialize(self):
	# 	return serialize('json', [self,], fields=('user', 'content', 'image'))		

	def serialize(self): # this is for making output as a list of json ---> making it cleaner than serialized data
		try:
			image = self.image.url
		except:
			image = ""
		
		data = {
			'user':self.user.id,
			'content':self.content,
			'image':image

		}

		json_data = json.dumps(data)

		return json_data