from django.db import models
from datetime import datetime


class CartesHearthstone(models.Model):
    nom = models.CharField(max_length=50, default="")
    prix = models.DecimalField(decimal_places=2, max_digits=10000)
    imageCarte = models.CharField(max_length=500, default="")
    dateToBD = models.DateField(default=datetime.now)

    def __str__(self):
        return self.nom + ' ' + str(self.prix) + '€'
