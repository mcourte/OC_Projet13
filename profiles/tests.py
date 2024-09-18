from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse
from django.test import TestCase, RequestFactory
from unittest.mock import patch, call
from django.http import Http404
from .views import index


class ProfileModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )

    def test_profile_str(self):
        """
        Tester la représentation en chaîne de caractères du profil.
        """
        self.assertEqual(str(self.profile), 'testuser')

    def test_profile_fields(self):
        """
        Tester les champs du modèle Profile.
        """
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.favorite_city, 'Test City')


class ProfileViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )
        self.factory = RequestFactory()

    def test_profiles_index_view(self):
        """
        Tester la vue d'index des profils.
        """
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_detail_view(self):
        """
        Tester la vue des détails d'un profil.
        """
        response = self.client.get(reverse('profiles:profile', args=['testuser']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Test City')

    @patch('profiles.views.Profile.objects.all')
    @patch('profiles.views.sentry_log')
    def test_no_profiles_found(self, mock_sentry_log, mock_all):
        # Créer un objet de requête HTTP factice
        request = self.factory.get('/profiles')
        # Simuler un utilisateur (peut être une instance de User si nécessaire)
        request.user = None

        # Simuler une liste vide de profils
        mock_all.return_value = []

        # Exécuter la vue
        with self.assertRaises(Http404):
            index(request)

        # Vérifier que la méthode sentry_log a été appelée avec les bons types et messages
        mock_sentry_log.assert_has_calls([
            call(error_type='message',
                 error_message="Requête d'index de profil initiée par l'utilisateur : None."
                 " URL : /profiles, Méthode : GET, Adresse IP : 127.0.0.1"),
            call(error_type='message', error_message='Aucun profil trouvé.')
        ])
