"""
Module contenant les patterns d'URL pour l'application 'oc_lettings_site'.

Ce module associe les chemins d'URL aux fonctions de vue correspondantes
pour l'application 'oc_lettings_site'.

Patterns d'URL :
    - '' : Mappe à la vue d'index, affichant la page d'accueil.
    - 'lettings/' : Inclut les patterns d'URL de l'application 'lettings'.
    - 'profiles/' : Inclut les patterns d'URL de l'application 'profiles'.
    - 'admin/' : Mappe à l'interface d'administration de Django.

Gestionnaires d'erreurs :
    - 404 : Vue pour la gestion des erreurs 404.
    - 500 : Vue pour la gestion des erreurs 500.
"""

from django.urls import path, include
from oc_lettings_site import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name="index"),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path("check_500/", views.error500, name="check_500"),
]
handler404 = views.error404
handler500 = views.error500
