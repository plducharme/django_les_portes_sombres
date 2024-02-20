from django.contrib import admin

# Register your models here.
from .models import Classe, Hero

admin.site.register(Classe)
admin.site.register(Hero)