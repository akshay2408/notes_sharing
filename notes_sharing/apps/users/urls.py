from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import UserViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
