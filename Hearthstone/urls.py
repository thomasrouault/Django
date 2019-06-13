from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hearthstone/', include('HearthstoneApp.urls')),
    path('purBeurre/<int:annee>/<int:mois>/<int:jour>', include('purBeurre.urls')),
]
