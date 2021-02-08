from django.db import models
from django.conf import settings


class Group(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='group_owner')
	members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_members')

	def __str__(self):
		return self.name
	

