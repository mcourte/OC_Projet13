"""
lettings/views.py

This module contains the Django view functions for displaying
listings of lettings and the details of individual lettings.
"""

from django.shortcuts import render
from lettings.models import Letting
from django.http import Http404
from oc_lettings_site.sentry_logger import sentry_log

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum,
# nulla eget feugiat sagittis, sem mi convallis eros, vitae dapibus nisi
# lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum
# lobortis quis. Phasellus eleifend ex auctor venenatis tempus.Aliquam vitae
# erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque
# iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque
# cursus id.


def index(request):
    """
        View function for displaying a list of lettings.
        This view retrieves all Letting objects from the database
        and passes them to the 'lettings/index.html' template.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse:The rendered HTML page displaying the list of lettings
        """

    sentry_log(
        error_type="message",
        error_message=(
            f"User request to display the lettings page: {request.user}"
            )
    )
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    response = render(request, 'lettings/index.html', context)
    sentry_log(
        error_type="message",
        error_message="Lettings page successfully returned.")
    return response

# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan
# porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus
# urna vulputate arcu, vitae efficitur lacus justo nec purus. Aenean finibus
# faucibus lectus at porta. Maecenas auctor, est ut luctus congue, dui enim
# mattis enim, ac condimentum velit libero in magna. Suspendisse potenti. In
# tempus a nisi sed laoreet.Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# vamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer
# vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.

# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan
# porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus
# urna vulputate arcu, vitae efficitur lacus justo nec purus. Aenean finibus
# faucibus lectus at porta. Maecenas auctor, est ut luctus congue, dui enim
# mattis enim, ac condimentum velit libero in magna. Suspendisse potenti. In
# tempus a nisi sed laoreet.Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# vamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer
# vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.


def letting(request, letting_id):
    """
        View function for displaying a single letting's details.
        This view retrieves a Letting object based on the provided letting_id
        and passes its details to the 'lettings/letting.html' template.

    Args:
        request: The HTTP request object.
        letting_id: The ID of the letting to be retrieved.

    Returns:
        HttpResponse: The rendered HTML page for the letting if found.
        If the letting does not exist or if a ValueError occurs,
        returns a 404 error page with an appropriate error message.
    """

    try:
        sentry_log(
            error_type="message",
            error_message=f"Letting request initiated by user: {request.user}")
        letting = Letting.objects.get(id=int(letting_id))
        context = {
             'title': letting.title,
             'address': letting.address,
        }
        sentry_log(
            error_type="message",
            error_message=f"Letting details found for ID: {letting_id}")
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        error = f"Letting id n°{letting_id} does not exist !"
        sentry_log(error_type="exception", error_message=error)

        raise Http404(error)
    except ValueError:
        error = f"ValueError : an number is requires but got : {letting_id}"
        sentry_log(error_type="error", error_message=error)
        raise Http404(error)
