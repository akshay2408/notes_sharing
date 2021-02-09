from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from notes_sharing.apps.test_data import TEST_DATA
from notes_sharing.apps.groups.models import Group


USER_ENDPOINT = '/notes_sharing/api/v1/users/'
GROUP_ENDPOINT = '/notes_sharing/api/v1/groups/'
USER_AUTHENTICATION = '/authenticate/'

class UserTestCase(APITestCase):
  def setUp(self):
    self.superuser = User.objects.create_superuser('admin@snow.com', 'adminpassword')
    self.client.force_authenticate(user=self.superuser)
    self.data = {'username': 'akshay@snow.com', 'first_name': 'Akshay', 'last_name': 'babar', 'password':'12345678'}

  def test_create_user(self):
    response = self.client.post(USER_ENDPOINT, self.data ,format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_user_token_authentication(self):
    self.client.post(USER_ENDPOINT, self.data ,format='json')
    credentails =  {'username': self.data.get('username') , 'password' : self.data.get('password') }
    response = self.client.post(USER_AUTHENTICATION, credentails ,format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(bool(response.data.get('token')), True)

  def test_user_joined_groups(self):
    group_ids = []
    for user in TEST_DATA["users"]:
      self.client.post(USER_ENDPOINT, user ,format='json')
    for group in TEST_DATA["groups"]:
      response = self.client.post(GROUP_ENDPOINT, group ,format='json')
      group_ids.append(response.data.get('id'))

    for group_id in group_ids:
      JOIN_GROUP_ENDPOINT = "{}{}{}".format(GROUP_ENDPOINT, group_id,"/join/")
      # before joining the group user does not exist in group member list. 
      self.assertEqual(bool(Group.objects.get(id=group_id).members.filter(id=self.superuser.id)), False)
      response = self.client.patch(JOIN_GROUP_ENDPOINT ,format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      # After joining the group user must be exist in group member list.
      self.assertEqual(bool(Group.objects.get(id=group_id).members.filter(id=self.superuser.id)), True)

    USER_JOINED_GROUP_ENDPOINT = "{}{}{}".format(USER_ENDPOINT, self.superuser.id,"/joined_groups/")
    response = self.client.get(USER_JOINED_GROUP_ENDPOINT ,format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
