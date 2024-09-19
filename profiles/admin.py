"""
Module contenant l'enregistrement des modèles pour l'application 'lettings'
dans l'interface d'administration Django.
"""

from django.contrib import admin
from profiles.models import Profile

# Enregistrement des modèles pour les rendre disponibles dans l'interface d'administration.

admin.site.register(Profile)
