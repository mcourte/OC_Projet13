"""
oc_lettings_site/views.py

This module contains the Django view functions for rendering the home
page of the application.
"""

from django.shortcuts import render
from oc_lettings_site.sentry_logger import sentry_log

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla
# eget feugiat sagittis, sem mi convallis eros,vitae dapibus nisi lorem
# dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis
# quis. Phasellus eleifend ex auctor venenatis tempus.Aliquam vitae erat ac
# orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim
# cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.


def index(request):
    """
        View function for displaying the home page.
        This view renders the 'index.html' template.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered HTML page for the home page.
        """
    sentry_log(
        error_type="message",
        error_message=(
          f"User-initiated request to display the home page : {request.user}")
    )
    response = render(request, "index.html")
    sentry_log(
        error_type="message",
        error_message="Home page successfully rendered.")
    return response


def error404(request, exception):
    error = f"404 error : {exception}"
    sentry_log(error_type="error", error_message=error)
    return render(request, "404.html", {'error': str(exception)})


def error500(request):
    error = "500 error"
    sentry_log(error_type="error", error_message=error)
    return render(request, "500.html")
