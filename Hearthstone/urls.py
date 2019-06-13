from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hearthstone/', include('HearthstoneApp.urls')),
    path('purBeurre/', include('purBeurre.urls')),
]
