from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from purBeurre.models import Article


def purBeurre_view(request):
    obj = Article.objects.only('titre').order_by('-date')[0:5]
    obj2 = Article.objects.latest('date')
    contexte = {"MenuArticleTitre": obj, "ArticlesContenu": obj2}
    return render(request, 'purBeurre.html', contexte)


def article_view(request, annee, mois, jour):
    objarticle = Article.objects.all().filter(date__year=annee).filter(date__month=mois).filter(date__day=jour)
    obj = Article.objects.only('titre').order_by('-date')[0:5]
    obj2 = Article.objects.latest('date')
    contexte = {"Articles": objarticle, "MenuArticleTitre": obj, "ArticlesContenu": obj2}
    return render(request, 'article.html', contexte)


def article_view(request, id):
    objarticle = get_object_or_404(Article, pk=id)
    contexte = {"Articles": objarticle}
    return render(request, 'article.html', contexte)
