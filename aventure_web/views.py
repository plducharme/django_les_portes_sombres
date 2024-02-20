from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from aventure_web.models import Classe, Hero
from .forms import SelectionHeroForm


# Create your views here.
def index(request):
    template = loader.get_template("aventure_web/index.html")

    liste_classes = Classe.objects.all()
    # On se construit un dictionnaire qui va contenir le "context" du template (les données que l'on veut utiliser
    # dans le template)
    context = {
        "classes": liste_classes
    }
    return HttpResponse(template.render(context, request))

def selection_hero(request):
    # Créer la form avec les données provenant du request
    form = SelectionHeroForm(request.POST)
    if form.is_valid():
        # sauvegarder le héro
        classe_hero = Classe.objects.get(id=form.classe_id)

        hero = Hero()
        hero.nom = form.nom_hero
        hero.classe = classe_hero
        hero.save()
        return HttpResponseRedirect("intro")
