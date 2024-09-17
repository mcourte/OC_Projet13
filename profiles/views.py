"""
profiles/views.py

This module contains the Django view functions for displaying
listings of usr profiles and the details of individual profiles.
"""

from django.shortcuts import render
from profiles.models import Profile
from django.http import Http404
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
        View function for displaying a list of user profiles.
        This view retrieves all Profile objects from the database
        and passes them to the 'profiles/index.html' template.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered HTML page displaying the list of
            user profiles.
        """
    sentry_log(
        error_type="message",
        error_message=f"User-initiated profile index query : {request.user}")
    profiles_list = Profile.objects.all()
    if not profiles_list:
        error = ("No profiles found.")
        raise Http404(error)
    context = {'profiles_list': profiles_list}
    sentry_log(
        error_type="message",
        error_message="List of profiles successfully retrieved.")
    return render(request, 'profiles/index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique
# senectus et netus et males


def profile(request, username):
    """
        View function for displaying a single user's profile details.
        This view retrieves a Profile object based on the provided username
        and passes its details to the 'profiles/profile.html' template.

        Args:
            request (HttpRequest): The HTTP request object.
            username (str): The username of the User whose profile is to
            be retrieved.

        Returns:
            HttpResponse: The rendered HTML page displaying the details of the
            user's profile.
            If the profiles does not exist returns a 404 error page with an
            appropriate error message.
        """
    try:
        sentry_log(
            error_type="message",
            error_message=f"Profile query initiated for the user : {username}")
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        error = (f"Profile Not Exist : Username {username} "
                 "does not exist !")

        raise Http404(error)

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
