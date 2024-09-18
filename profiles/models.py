"""
Ce module contient les modèles de données pour l'application 'profiles',
définissant la structure du profil utilisateur.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Modèle représentant un profil utilisateur.

    Attributs :
        user (User) : Une relation one-to-one avec le modèle User.
            Si l'utilisateur est supprimé, le profil est également supprimé.
        favorite_city (str) : Un champ optionnel pour la ville préférée de l'utilisateur,
            avec une longueur maximale de 64 caractères.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profiles_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Retourne une représentation en chaîne de caractères du profil."""
        return self.user.username
