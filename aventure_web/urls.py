from django.urls import path

from . import views

# On ajouter la variable app_name pour indiquer le namespace dans lequel on se trouve
# Voir django_les_portes_sombres/urls.py
app_name = "aventure"

urlpatterns = [
    path("", views.index, name="index"),
    path("selection-hero", views.selection_hero, name="selection"),
]