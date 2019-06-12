from django.contrib import admin
from django.urls import path
from HearthstoneApp.views import cartes_view
from HearthstoneApp.views import accueil_view
from HearthstoneApp.views import purBeurre_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cartes/', cartes_view, name="Cartes"),
    path('', accueil_view, name="Accueil"),
    path('purBeurre/', purBeurre_view, name="Pur Beurre")
]
