from django.urls import path

from . import views

urlpatterns = [
    path("", views.eco_api, name="eco_api"),
]