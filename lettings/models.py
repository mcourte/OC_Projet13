"""
Module contenant les modèles de données pour l'application 'lettings',
définissant la structure des entités Address et Letting dans la base de données.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Modèle représentant une adresse physique.

    Attributs :
        number (PositiveIntegerField) : Le numéro de rue de l'adresse,
            doit être un entier positif et ne pas dépasser 9999.
        street (CharField) : Le nom de la rue, limité à 64 caractères.
        city (CharField) : Le nom de la ville, limité à 64 caractères.
        state (CharField) : Le code de l'état, limité à 2 caractères.
        zip_code (PositiveIntegerField) : Le code postal, doit être un entier
            positif et ne pas dépasser 99999.
        country_iso_code (CharField) : Le code ISO du pays, limité à 3 caractères.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)]
    )
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """Retourne une représentation sous forme de chaîne de l'adresse."""
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """Modèle représentant une location immobilière.

    Attributs :
        title (CharField) : Le titre de la location, limité à 256 caractères.
        address (OneToOneField) : Une relation un-à-un avec le modèle Address,
        représentant le lieu de la location.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Retourne une représentation sous forme de chaîne de la location."""
        return self.title
