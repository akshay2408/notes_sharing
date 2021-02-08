from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import NotesViewSet

router = routers.SimpleRouter()
router.register('notes', NotesViewSet)
urlpatterns = router.urls
