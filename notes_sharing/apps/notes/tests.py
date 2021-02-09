from rest_framework.test import APITestCase
from notes_sharing.apps.notes.models import Notes
from rest_framework import status
from django.contrib.auth.models import User
from notes_sharing.apps.test_data import TEST_DATA

GROUP_ENDPOINT = '/notes_sharing/api/v1/groups/'
USER_ENDPOINT = '/notes_sharing/api/v1/users/'


class NotesTestCase(APITestCase):
  def setUp(self):
    self.superuser = User.objects.create_superuser('admin@snow.com', 'adminpassword')
    self.client.force_authenticate(user=self.superuser)
    for user in TEST_DATA["users"]:
      self.client.post(USER_ENDPOINT, user ,format='json')
    for group in TEST_DATA["groups"]:
      self.client.post(GROUP_ENDPOINT, group ,format='json')

  def test_create_notes(self):
    response = self.client.post('/notes_sharing/api/v1/notes/', TEST_DATA.get("notes")[0] ,format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


