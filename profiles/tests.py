from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse
from django.test import TestCase


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
