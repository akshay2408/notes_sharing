from rest_framework.test import APITestCase
from notes_sharing.apps.groups.models import Group
from notes_sharing.apps.users.models import User
from rest_framework import status
from notes_sharing.apps.test_data import TEST_DATA

USER_ENDPOINT = '/notes_sharing/api/v1/users/'
GROUP_ENDPOINT = '/notes_sharing/api/v1/groups/'

class GroupTestCase(APITestCase):
  def setUp(self):
    self.superuser = User.objects.create_superuser('admin@snow.com', 'adminpassword')
    self.client.login(username='admin@snow.com', password='adminpassword')
    self.group_ids = []
    for user in TEST_DATA["users"]:
      self.client.post(USER_ENDPOINT, user ,format='json')
    for group in TEST_DATA["groups"]:
      response = self.client.post(GROUP_ENDPOINT, group ,format='json')
      self.group_ids.append(response.data.get('id'))
    
  def test_create_group(self):
    response = self.client.post(GROUP_ENDPOINT, TEST_DATA.get("groups")[0] ,format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_join_group_by_user(self):
    for group_id in self.group_ids:
      JOIN_GROUP_ENDPOINT = "{}{}{}".format(GROUP_ENDPOINT, group_id,"/join/")
      # before joining the group user does not exist in group member list. 
      self.assertEqual(bool(Group.objects.get(id=group_id).members.filter(id=self.superuser.id)), False)
      response = self.client.patch(JOIN_GROUP_ENDPOINT ,format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      # After joining the group user must be exist in group member list.
      self.assertEqual(bool(Group.objects.get(id=group_id).members.filter(id=self.superuser.id)), True)
