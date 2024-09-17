"""
profiles/url.py

This module contains the URL patterns for the 'profiles' application,
mapping URL paths to their corresponding view functions.
URL Patterns:
    - 'profiles/' : Maps to the index view, displaying the list of profiles.
    - '<profiles/str:username>/' : Maps to the profile view, displaying the
    details of a specific profile based on the username.
"""
from django.urls import path
from profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<str:username>/", views.profile, name="profile"),
]
