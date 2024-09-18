"""
lettings/views.py

Ce module contient les fonctions de vue Django pour afficher les
listes des annonces et les détails des annonces individuelles.
"""
import os
import sys
from django.shortcuts import render
from lettings.models import Letting
from django.http import Http404
# Déterminez le chemin absolu du répertoire parent
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../'))

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.insert(0, parent_dir)

from sentry_logger import sentry_log


def index(request):
    """
    Fonction de vue pour afficher la liste des annonces.
    Cette vue récupère tous les objets Letting depuis la base de données
    et les passe au modèle 'lettings/index.html'.

    Args:
        request (HttpRequest): L'objet de requête HTTP.

    Returns:
        HttpResponse: La page HTML rendue affichant la liste des annonces.
    """
    sentry_log(
        error_type="message",
        error_message=(
            f"Requête initiée par l'utilisateur pour afficher la page des biens : {request.user}. "
            f"URL : {request.path}, "
            f"Méthode : {request.method}, "
            f"Adresse IP : {request.META.get('REMOTE_ADDR')}"
        )
    )
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    response = render(request, 'lettings/index.html', context)
    sentry_log(
        error_type="message",
        error_message="Page des biens rendue avec succès."
    )
    return response


def letting(request, letting_id):
    """
    Fonction de vue pour afficher les détails d'une annonce spécifique.
    Cette vue récupère un objet Letting basé sur l'ID fourni
    et passe ses détails au modèle 'lettings/letting.html'.

    Args:
        request: L'objet de requête HTTP.
        letting_id: L'ID de l'annonce à récupérer.

    Returns:
        HttpResponse: La page HTML rendue pour l'annonce si elle est trouvée.
        Si l'annonce n'existe pas ou si une ValueError se produit,
        retourne une page d'erreur 404 avec un message d'erreur approprié.
    """
    try:
        sentry_log(
            error_type="message",
            error_message=f"Requête de bien initiée par l'utilisateur : {request.user}")
        letting = Letting.objects.get(id=int(letting_id))
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        sentry_log(
            error_type="message",
            error_message=f"Détails du bien trouvés pour l'ID : {letting_id}")
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        error = f"Le bien avec l'id n°{letting_id} n'existe pas !"
        sentry_log(error_type="exception", error_message=error)
        raise Http404(error)
    except ValueError:
        error = f"ValueError : un nombre est requis mais reçu : {letting_id}"
        sentry_log(error_type="error", error_message=error)
        raise Http404(error)
