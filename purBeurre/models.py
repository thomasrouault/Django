from django.db import models
from datetime import datetime


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
