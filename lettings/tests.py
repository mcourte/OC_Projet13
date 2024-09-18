from django.test import TestCase
from lettings.models import Address
from django.urls import reverse
from lettings.models import Letting


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
        Configuration des tests : Création d'un objet Address et d'un objet Letting pour les tests.
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
        Configuration des tests : Création d'un objet Address et d'un objet Letting pour les tests.
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
