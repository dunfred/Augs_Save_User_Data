from django.urls import path, include
from .views import create_user_view

urlpatterns = [
    path('', create_user_view, name="create"),
]
