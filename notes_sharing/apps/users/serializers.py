from rest_framework.serializers import (ModelSerializer, CharField)
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
	password = CharField( style={'input_type': 'password'}, write_only=True)
	class Meta:
			model = User
			fields = ["id", "first_name", "last_name", "email", "password",]

	def validate_password(self, password):
			return make_password(password)