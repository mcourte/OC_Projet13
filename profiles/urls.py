"""
profiles/urls.py

Ce module contient les modèles d'URL pour l'application 'profiles',
en mappant les chemins d'URL à leurs fonctions de vue correspondantes.
Modèles d'URL :
    - 'profiles/' : Mappe à la vue d'index, affichant la liste des profils.
    - '<str:username>/' : Mappe à la vue du profil, affichant les détails
      d'un profil spécifique basé sur le nom d'utilisateur.
"""
from django.urls import path
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
