from django.http import HttpResponse
from django.shortcuts import render
from purBeurre.models import Article


def purBeurre_view(request):
    obj = Article.objects.only('titre').order_by('-date')[0:5]
    obj2 = Article.objects.latest('date')
    contexte = {"ArticlesTitre": obj, "ArticlesContenu": obj2}
    return render(request, 'purBeurre.html', contexte)


def article_view(request, annee, mois, jour):
    obj = Article.objects.all().filter(date__gt='2019-06-12')
    contexte = {"Article": obj}
    return render(request, 'article.html', contexte)
