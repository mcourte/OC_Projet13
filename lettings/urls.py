"""
lettings/urls.py

This module contains the URL patterns for the 'lettings' application,
mapping URL paths to their corresponding view functions.
URL Patterns:
    - 'lettings/"' : Maps to the index view, displaying the list of lettings.
    - 'lettings/<letting_id>/' : Maps to the letting view, displaying the
       details of a specific letting based on its ID.

Namespaces:
    - app_name: The namespace for the 'lettings' application.
"""

from django.urls import path
from lettings import views

app_name = "lettings"
urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<letting_id>/", views.letting, name="letting"),
]
