from django.http import HttpResponse
from django.shortcuts import render
from HearthstoneApp.models import CartesHearthstone, Article


def cartes_view(request):
    obj = CartesHearthstone.objects.all().order_by('nom')
    contexte = {"CartesHearthStone": obj}
    return render(request, 'cartes.html', contexte)


def cartesPersonne_view(request):
    obj2 = CartesHearthstone.objects.all().order_by('nom').filter(couleur__istartswith='black').exclude(
        nom__icontains='Brigitte')
    contexte2 = {"CartesPersonnes": obj2}
    return render(request, 'cartesPersonnes.html', contexte2)


def accueil_view(request):
    utilisateur = request.user
    return render(request, 'accueil.html', {})


def purBeurre_view(request):
    obj = Article.objects.only('titre').order_by('-date')[0:5]
    obj2 = Article.objects.latest('date')
    contexte = {"ArticlesTitre": obj, "ArticlesContenu": obj2}
    return render(request, 'purBeurre.html', contexte)
