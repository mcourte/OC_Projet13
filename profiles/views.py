"""
profiles/views.py

Ce module contient les fonctions de vue Django pour afficher
les listes de profils utilisateur et les détails des profils individuels.
"""
import os
import sys
from django.shortcuts import render
from profiles.models import Profile
from django.http import Http404
# Déterminez le chemin absolu du répertoire parent
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../'))

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.insert(0, parent_dir)

from sentry_logger import sentry_log


def index(request):
    """
    Fonction de vue pour afficher une liste de profils utilisateur.
    Cette vue récupère tous les objets Profile de la base de données
    et les passe au modèle 'profiles/index.html'.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La page HTML rendue affichant la liste des profils
        utilisateur.
    """
    sentry_log(
        error_type="message",
        error_message=(
            f"Requête d'index de profil initiée par l'utilisateur : {request.user}. "
            f"URL : {request.path}, "
            f"Méthode : {request.method}, "
            f"Adresse IP : {request.META.get('REMOTE_ADDR')}"
        )
    )
    profiles_list = Profile.objects.all()
    if not profiles_list:
        error = "Aucun profil trouvé."
        sentry_log(
            error_type="message",
            error_message=error
        )
        raise Http404(error)
    context = {'profiles_list': profiles_list}
    sentry_log(
        error_type="message",
        error_message="Liste des profils récupérée avec succès."
    )
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Fonction de vue pour afficher les détails du profil d'un utilisateur.
    """
    try:
        sentry_log(
            error_type="message",
            error_message=f"Requête de profil initiée pour l'utilisateur : {username}")
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        error = (f"Profil non existant : Le nom d'utilisateur {username} "
                 "n'existe pas !")
        raise Http404(error)

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
