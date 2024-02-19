from django.db import models


# Create your models here.
# Les classes modélisées seront persistées dans une BD (sauf les classes abstraites)
# Voir https://docs.djangoproject.com/en/5.0/topics/db/models/
class Classe(models.Model):
    nom = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    # Va contenir le path vers l'image de la classe
    path_image = models.CharField(max_length=255)


class Hero(models.Model):
    nom = models.CharField(max_length=50)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)



