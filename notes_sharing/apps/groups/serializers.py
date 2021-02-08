from rest_framework.serializers import (ModelSerializer, CurrentUserDefault, HiddenField, SerializerMethodField)
from .models import Group
from notes_sharing.apps.notes.serializers import NotesSerializer

class GroupSerializer(ModelSerializer):
	owner = HiddenField(default=CurrentUserDefault())

	class Meta:
		model=Group
		fields='__all__'


class GroupDetailSerializer(GroupSerializer):
	notes = SerializerMethodField(read_only=True)

	def get_notes(self, obj):
		notes = obj.notes_groups.all()
		serializer = NotesSerializer(notes, many=True)
		return serializer.data
