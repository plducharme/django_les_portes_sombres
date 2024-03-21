"""
URL configuration for django_les_portes_sombres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import aventure_web.views

# Ceci défini le "context root" de l'application
# ex: http://127.0.0.1:8000/admin ouvre l'application d'administration
# http://127.0.0.1:8000/aventure ouvre notre application "aventure_web" (aussi un package python) et prend les configs
# de son fichier urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', aventure_web.views.index),
    path("aventure/", include(("aventure_web.urls", "aventure_web"), namespace="aventure")),
]
