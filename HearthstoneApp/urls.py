from django.contrib import admin
from django.urls import path

from HearthstoneApp.views import accueil_view, cartesPersonne_view, cartes_view

urlpatterns = [
    path('', accueil_view, name="Accueil"),
    path('cartesHearthStone/', cartes_view, name="Cartes HearthStone"),
    path('cartesPersonnes/', cartesPersonne_view, name="Cartes Personnes"),
]
