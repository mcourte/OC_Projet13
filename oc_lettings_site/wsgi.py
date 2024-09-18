"""
Configuration WSGI pour le projet 'oc_lettings_site'.

Ce module expose l'application WSGI callable comme une variable `application`.
Il configure le projet Django pour le déploiement avec des serveurs WSGI.

Modules importés :
    - `os` : Pour gérer les paramètres d'environnement.
    - `get_wsgi_application` : Pour obtenir l'application WSGI de Django.

Variables :
    - `application` : L'application WSGI callable exposée pour le serveur WSGI.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
