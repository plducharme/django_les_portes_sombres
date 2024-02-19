from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template("aventure_web/index.html")
    # TODO Modéliser heros
    liste_heros = []
    # On se construit un dictionnaire qui va contenir le "context" du template (les données que l'on veut utiliser
    # dans le template)
    context = {
        "heros": [],
    }
    return HttpResponse(template.render(context, request))