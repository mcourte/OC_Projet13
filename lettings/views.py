"""
lettings/views.py

Ce module contient les fonctions de vue Django pour afficher les
listes des annonces et les détails des annonces individuelles.
"""

from django.shortcuts import render
from lettings.models import Letting
from django.http import Http404


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
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    response = render(request, 'lettings/index.html', context)
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
        letting = Letting.objects.get(id=int(letting_id))
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        error = f"L'annonce avec l'ID n°{letting_id} n'existe pas !"
        raise Http404(error)
    except ValueError:
        error = f"ValueError : un nombre est requis mais reçu : {letting_id}"
        raise Http404(error)
