from django.test import TestCase, RequestFactory
from lettings.models import Address
from django.urls import reverse
from lettings.models import Letting
from unittest.mock import patch, call
from django.http import Http404
from .views import letting


class AddressModelTests(TestCase):
    """
    Tests pour le modèle Address.
    """

    def setUp(self):
        """
        Configuration des tests : Création d'un objet Address pour les tests.
        """
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )

    def test_address_str(self):
        """
        Test de la représentation en chaîne du modèle Address.
        """
        self.assertEqual(str(self.address), "123 Test Street")

    def test_address_fields(self):
        """
        Test des champs du modèle Address.
        """
        self.assertEqual(self.address.number, 123)
        self.assertEqual(self.address.street, 'Test Street')
        self.assertEqual(self.address.city, 'Test City')
        self.assertEqual(self.address.state, 'TS')
        self.assertEqual(self.address.zip_code, 12345)
        self.assertEqual(self.address.country_iso_code, 'TST')

    def test_address_invalid_number(self):
        """
        Test d'un numéro invalide dépassant la valeur maximale autorisée.
        """
        with self.assertRaises(ValueError):
            Address.objects.create(
                number='A',
                street='Invalid Street',
                city='Invalid City',
                state='IS',
                zip_code=9999,
                country_iso_code='INV'
            )


class LettingModelTests(TestCase):
    """
    Tests pour le modèle Letting.
    """

    def setUp(self):
        """
        Configuration des tests : Création d'un objet Address
        et d'un objet Letting pour les tests.
        """
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )

    def test_letting_str(self):
        """
        Test de la représentation en chaîne du modèle Letting.
        """
        self.assertEqual(str(self.letting), "Test Letting")

    def test_letting_fields(self):
        """
        Test des champs du modèle Letting.
        """
        self.assertEqual(self.letting.title, 'Test Letting')
        self.assertEqual(self.letting.address, self.address)


class LettingViewTests(TestCase):
    """
    Tests pour les vues du modèle Letting.
    """

    def setUp(self):
        """
        Configuration des tests : Création d'un objet Address
        et d'un objet Letting pour les tests.
        """
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )
        self.factory = RequestFactory()

    def test_lettings_index_view(self):
        """
        Test de la vue d'index des annonces.
        """
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, 'Test Letting')

    def test_letting_detail_view(self):
        """
        Test de la vue de détail d'une annonce.
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, 'Test Street')

    @patch('lettings.views.Letting.objects.get')
    @patch('lettings.views.sentry_log')
    def test_value_error(self, mock_sentry_log, mock_get):
        # Créer un objet de requête HTTP factice
        request = self.factory.get('/letting/1')
        # Simuler un utilisateur (peut être une instance de User si nécessaire)
        request.user = None

        # Simuler une ValueError
        mock_get.side_effect = ValueError

        # Exécuter la vue
        with self.assertRaises(Http404):
            letting(request, 'invalid_id')

        # Vérifier que la méthode sentry_log a été appelée une fois avec le bon type et message
        mock_sentry_log.assert_has_calls([
            call(error_type="message",
                 error_message="Requête de bien initiée par l'utilisateur : None"),
            call(error_type="error",
                 error_message="ValueError : un nombre est requis mais reçu : invalid_id")
        ])
