"""
profiles/models.py

This module contains the data models for the 'profiles' application,
defining the structure of user.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model representing a profile.

    Attributes:
        user (User): A one-to-one relationship with the User model.
        If User is deleted, the Profile is also deleted.
        favorite_city (str): An optional field for the user's favorite city,
        with a maximum length of 64 characters.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profiles_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
