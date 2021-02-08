from rest_framework.viewsets import ModelViewSet 
from .serializers import UserSerializer
from .models import User
from notes_sharing.apps.groups.serializers import GroupSerializer, NotesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from notes_sharing.apps.notes.models import Notes 
from django.db.models import Q


class UserViewSet(ModelViewSet):
	serializer_class=UserSerializer
	queryset=User.objects.all()
	
	@action(detail=True, methods=['get'])
	def joined_groups(self, request, pk=None):
		groups = self.get_object().group_members.all()
		serializer = GroupSerializer(groups, many=True)
		return Response(serializer.data)
	
	@action(detail=True, methods=['get'])
	def owned_groups(self, request, pk=None):
		groups = self.get_object().group_owner.all()
		serializer = GroupSerializer(groups, many=True)
		return Response(serializer.data)

	@action(detail=False, methods=['get'])
	def shared_notes(self, request, pk=None):		
		notes = Notes.objects.filter(Q(groups__members__in=[self.request.user]) | Q(groups__owner=self.request.user) )
		serializer = NotesSerializer(notes, many=True)
		return Response(serializer.data)
