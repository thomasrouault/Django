from django.contrib import admin
from django.urls import path
from HearthstoneApp.views import cartes_view
from HearthstoneApp.views import cartesPersonne_view
from HearthstoneApp.views import accueil_view
from HearthstoneApp.views import purBeurre_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cartesHearthStone/', cartes_view, name="Cartes HearthStone"),
    path('cartesPersonnes/', cartesPersonne_view, name="Cartes Personnes"),
    path('', accueil_view, name="Accueil"),
    path('purBeurre/', purBeurre_view, name="Pur Beurre")
]
