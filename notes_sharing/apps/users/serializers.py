from rest_framework.serializers import (ModelSerializer, CharField, BooleanField)
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
	password = CharField( style={'input_type': 'password'}, write_only=True)
	is_staff = BooleanField(default=True)
	class Meta:
			model = User
			fields = ["id", "first_name", "last_name", "username", "password", 'is_staff']

	def validate_password(self, password):
			return make_password(password)