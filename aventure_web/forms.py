from django import forms
from random import choice


# Voir https://docs.djangoproject.com/en/5.0/topics/forms/
class SelectionHeroForm(forms.Form):

    @staticmethod
    def generer_nom():
        return choice(["Ariala", "Helvetico", "Wing Ding"])

    nom_hero = forms.CharField(max_length=50, min_length=1, empty_value=generer_nom(), label="Nom du héro")
    classe_id = forms.IntegerField()

