from rest_framework.viewsets import ModelViewSet 
from .serializers import NotesSerializer
from .models import Notes

class NotesViewSet(ModelViewSet):
	serializer_class=NotesSerializer
	queryset=Notes.objects.all()

	def get_queryset(self, *args, **kwargs):
		return Notes.objects.filter(created_by=self.request.user)
		