from django.shortcuts import render
import os
import sys

# Déterminez le chemin absolu du répertoire parent
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../'))

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.insert(0, parent_dir)

from sentry_logger import sentry_log


def index(request):
    """
    Fonction de vue pour afficher la page d'accueil.

    Cette vue rend le template 'index.html'.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La page HTML rendue pour la page d'accueil.
    """
    sentry_log(
        error_type="message",
        error_message=(
            f"Requête initiée par l'utilisateur pour afficher la page d'accueil : {request.user}. "
            f"URL : {request.path}, "
            f"Méthode : {request.method}, "
            f"Adresse IP : {request.META.get('REMOTE_ADDR')}"
        )
    )
    response = render(request, "index.html")
    sentry_log(
        error_type="message",
        error_message="Page d'accueil rendue avec succès."
    )
    return response


def error404(request, exception):
    """
    Fonction de vue pour gérer les erreurs 404.

    Cette vue rend le template '404.html' et fournit un message d'erreur.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.
        exception (Exception): L'exception qui a causé l'erreur 404.

    Returns:
        HttpResponse: La page HTML rendue pour l'erreur 404, avec le message d'erreur.
    """
    error = f"404 error : {exception}"
    sentry_log(
        error_type="error",
        error_message=(
            f"{error}. "
            f"URL : {request.path}, "
            f"Méthode : {request.method}, "
            f"Adresse IP : {request.META.get('REMOTE_ADDR')}"
        )
    )
    return render(request, "404.html", {'error': str(exception)})


def error500(request):
    """
    Fonction de vue pour gérer les erreurs 500.

    Cette vue rend le template '500.html' et fournit un message d'erreur.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La page HTML rendue pour l'erreur 500, avec le message d'erreur.
    """
    error = "500 error"
    sentry_log(
        error_type="error",
        error_message=(
            f"{error}. "
            f"URL : {request.path}, "
            f"Méthode : {request.method}, "
            f"Adresse IP : {request.META.get('REMOTE_ADDR')}"
        )
    )
    return render(request, "500.html")
