"""
profiles/views.py

Ce module contient les fonctions de vue Django pour afficher
les listes de profils utilisateur et les détails des profils individuels.
"""

from django.shortcuts import render, get_object_or_404
from profiles.models import Profile
from django.http import Http404


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
    profiles_list = Profile.objects.all()
    if not profiles_list:
        error = "Aucun profil trouvé."
        raise Http404(error)
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Fonction de vue pour afficher les détails du profil d'un utilisateur.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
