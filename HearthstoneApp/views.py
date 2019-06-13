from django.http import HttpResponse
from django.shortcuts import render
from HearthstoneApp.models import CartesHearthstone


def cartes_view(request):
    obj = CartesHearthstone.objects.all().order_by('nom')
    contexte = {"CartesHearthStone": obj}
    return render(request, 'cartes.html', contexte)


def cartesPersonne_view(request):
    obj = CartesHearthstone.objects.all().order_by('nom').filter(couleur__istartswith='black').exclude(
        nom__icontains='Brigitte')
    contexte = {"CartesPersonnes": obj}
    return render(request, 'cartesPersonnes.html', contexte)


def accueil_view(request):
    utilisateur = request.user
    return render(request, 'accueil.html', {})

