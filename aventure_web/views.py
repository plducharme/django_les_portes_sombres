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
    # dans le template pour cette "request")
    context = {
        "classes": liste_classes
    }
    return HttpResponse(template.render(context, request))


def selection_hero(request):
    # Créer la form avec les données provenant du request
    form = SelectionHeroForm(request.POST)
    if form.is_valid():
        # Aller chercher l'objet de la Classe sélectionnée à partir de la BD
        classe_hero = Classe.objects.get(id=form.data['classe_id'])

        hero = Hero()
        hero.nom = form.data['nom_hero']
        hero.classe = classe_hero
        hero.save()
        request.session['nom_hero'] = hero.nom
        return HttpResponseRedirect("intro")
    else:
        return index(request)


def intro(request):
    template = loader.get_template("aventure_web/intro.html")
    context = {
        'nom_hero' : request.session.get('nom_hero'),
    }
    return HttpResponse(template.render(context, request))



