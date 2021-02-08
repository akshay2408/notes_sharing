from django.db import models
from django.conf import settings
from notes_sharing.apps.groups.models import Group

class Notes(models.Model):
	title = models.CharField(max_length=50, blank=False, null=False)
	description = models.TextField(max_length=5000, blank=False, null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes_owner')
	groups = models.ManyToManyField(Group, related_name='notes_groups', blank=True)

	def __str__(self):
		return self.title
