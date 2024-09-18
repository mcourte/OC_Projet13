"""
Configuration ASGI pour le projet Django.

Ce module expose l'application ASGI callable comme une variable
`application`, qui est utilisée pour gérer les connexions HTTP et WebSocket
dans le projet Django.
"""

import os

from django.core.asgi import get_asgi_application

# Définir le module de configuration des paramètres Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

# Obtenir l'application ASGI callable.
application = get_asgi_application()
