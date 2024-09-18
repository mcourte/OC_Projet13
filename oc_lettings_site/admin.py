"""
Module contenant l'enregistrement des modèles pour l'application 'lettings'
dans l'interface d'administration Django.
"""

from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address
from profiles.models import Profile

# Enregistrement des modèles pour les rendre disponibles dans l'interface d'administration.
admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
