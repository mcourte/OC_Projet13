from django.shortcuts import render


def index(request):
    """
    Fonction de vue pour afficher la page d'accueil.

    Cette vue rend le template 'index.html'.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La page HTML rendue pour la page d'accueil.
    """
    response = render(request, "index.html")
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

    return render(request, "500.html")
