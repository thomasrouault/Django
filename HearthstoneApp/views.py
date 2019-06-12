from django.http import HttpResponse
from django.shortcuts import render


def cartes_view(request):
    utilisateur = request.user
    return render(request, 'cartes.html', {})


def accueil_view(request):
    utilisateur = request.user
    return render(request, 'accueil.html', {})


def purBeurre_view(request):
    utilisateur = request.user
    return render(request, 'purBeurre.html', {})
