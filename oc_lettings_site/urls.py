"""
oc_lettings_site/urls.py

This module contains the URL patterns for the 'oc_lettings_site' application,
mapping URL paths to their corresponding view functions.
URL Patterns:
    - '' : Maps to the index view, displaying the home page.
    - 'lettings/' : Includes the URL patterns from the 'lettings' application.
    - 'profiles/' : Includes the URL patterns from the 'profiles' application.
    - 'admin/' : Maps to the Django admin interface.
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
    path("check_500/", views.error500, name="check_500"),
]
handler404 = views.error404
handler500 = views.error500
