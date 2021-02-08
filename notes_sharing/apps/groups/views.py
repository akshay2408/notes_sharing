from rest_framework.viewsets import ModelViewSet 
from .serializers import GroupSerializer, GroupDetailSerializer
from .models import Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (
  HTTP_200_OK,
  HTTP_400_BAD_REQUEST,)
from notes_sharing.apps.notes.serializers import NotesSerializer


class GroupViewSet(ModelViewSet):
  serializer_class=GroupSerializer
  queryset=Group.objects.all()

  def get_queryset(self, *args, **kwargs):
    if self.action in ['list', 'retrieve', 'join']:
      return self.queryset
    return Group.objects.filter(owner=self.request.user)


  @action(detail=True, methods=['patch'])
  def join(self, request, pk=None):
    group = self.get_object()
    if not request.user.is_anonymous:
      group.members.add(request.user.id)
      return Response({'success':'Group joined successfully.'}, status=HTTP_200_OK)
    else:
      return Response({'error':'User must be logged-in.'},status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_400_BAD_REQUEST)


