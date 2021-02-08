from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import GroupViewSet

router = routers.SimpleRouter()
router.register('groups', GroupViewSet)
urlpatterns = router.urls
