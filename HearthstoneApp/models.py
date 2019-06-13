from django.db import models
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
