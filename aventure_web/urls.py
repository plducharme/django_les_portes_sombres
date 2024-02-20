from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/aventure/selection-hero", views.index, name="index"),
]