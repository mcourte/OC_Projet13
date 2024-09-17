"""
lettings/models.py

This module contains the data models for the 'lettings' application,
defining the structure of Address and Letting entities in the database.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Model representing a physical address.

    Attributes:
        number (PositiveIntegerField): The street number of the address,
            must be a positive integer and not exceed 9999.
        street (CharField): The name of the street, limited to 64 characters.
        city (CharField): The name of the city, limited to 64 characters.
        state (CharField): The state code, limited to 2 characters.
        zip_code (PositiveIntegerField): The postal code, must be a positive
            integer and not exceed 99999.
        country_iso_code (CharField): The ISO code of the country, limited
            to 3 characters.
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
        """Return a string representation of the address."""
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """Model representing a property letting.

    Attributes:
        title (CharField): The title of the letting, limited to 256 characters.
        address (OneToOneField): A one-to-one relationship with the Address
        model, representing the location of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the letting."""
        return self.title
