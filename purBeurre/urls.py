from django.contrib import admin
from django.urls import path

from purBeurre.views import article_view

urlpatterns = [

    path('', article_view, name=""),
    path('1/', article_view, name="Article 1"),
]
