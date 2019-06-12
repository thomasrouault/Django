from django.db import models
from django import forms
from datetime import datetime

FAVORITE_COLORS_CHOICES = [
    ('', ''),
    ('green', 'Green'),
    ('red', 'Red'),
    ('black', 'Black'),
    ('white', 'White'),
    ('blue', 'Blue'),
]

TIME_ZONE = 'Europe/Paris'


class CartesHearthstone(models.Model):
    nom = models.CharField(max_length=50, default="")
    prix = models.DecimalField(decimal_places=2, max_digits=10000, null=True, blank=True)
    imageCarte = models.CharField(max_length=500, default="")
    couleur = models.CharField(max_length=20, choices=FAVORITE_COLORS_CHOICES, default="", null=True, blank=True)
    dateToBD = models.DateField(default=datetime.now)

    def __str__(self):
        return self.nom + ' ' + str(self.prix) + '€'


class Auteur(models.Model):
    nom = models.CharField(max_length=50, default="")
    prenom = models.CharField(max_length=50, default="")
    dateDeNaissance = models.DateField(default=datetime.now)
    pseudo = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.nom + ' ' + self.prenom


class Article(models.Model):
    titre = models.CharField(max_length=50, default="")
    contenu = models.TextField(default="")
    date = models.DateTimeField(default=datetime.now)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre + ' ' + self.auteur.prenom
