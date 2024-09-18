"""
Module contenant les motifs d'URL pour l'application 'lettings',
mappant les chemins d'URL aux fonctions de vue correspondantes.

Motifs d'URL :
    - 'lettings/"' : Mappe vers la vue d'index, affichant la liste des annonces.
    - 'lettings/<letting_id>/' : Mappe vers la vue de détail d'une annonce, affichant
      les détails d'une annonce spécifique en fonction de son ID.

Espaces de noms :
    - app_name : L'espace de noms pour l'application 'lettings'.
"""

from django.urls import path
from lettings import views

app_name = "lettings"
urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<letting_id>/", views.letting, name="letting"),
]
