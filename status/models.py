from django.db import models
from django.conf import settings

def upload_status_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass


class StatusManger(models.Manager):
    def get_queryset(self):
	    return StatusQuerySet(self.model, using=self._db)


# Create your models here.


class Status(models.Model):  # similar to social media status
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	objects = StatusManger()


	def __str__(self):
		return str(self.content)[:50]

	class meta:
		verbose_name='Status Post'
		verbose_name_plural='Status Posts'