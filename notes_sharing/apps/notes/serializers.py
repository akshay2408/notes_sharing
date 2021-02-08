from rest_framework.serializers import (ModelSerializer, SerializerMethodField, CurrentUserDefault, HiddenField)
from .models import Notes

class NotesSerializer(ModelSerializer):
	created_by = HiddenField(default=CurrentUserDefault())

	class Meta:
		model=Notes
		fields=['id', 'title', 'description', 'created_by', 'groups']

	