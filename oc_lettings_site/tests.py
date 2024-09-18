import os
import sys
from django.test import TestCase, override_settings, Client
from django.urls import reverse
from unittest.mock import patch

# Déterminez le chemin absolu du répertoire parent
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../'))

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.insert(0, parent_dir)

from sentry_logger import sentry_log


class IndexViewTests(TestCase):
    """
    Tests pour la vue d'index.

    Ces tests vérifient que la vue d'index affiche correctement la page d'accueil
    et utilise le modèle de template attendu.
    """

    def test_index_view(self):
        """
        Test de la vue d'index.

        Ce test envoie une requête GET à l'URL d'index et vérifie que le code
        de statut HTTP est 200. Il vérifie également que le modèle de template
        utilisé est 'index.html'.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class Error500ViewTests(TestCase):
    """
    Test de la vue d'erreur 500.

    Ce test envoie une requête GET à une URL qui provoque une erreur 500
    et vérifie que le code de statut HTTP est 200 (même en cas d'erreur).
    Il vérifie également que le modèle de template utilisé est '500.html'.
    """
    @override_settings(DEBUG=False)
    @patch('oc_lettings_site.views.sentry_log')
    def test_error500_view(self, mock_sentry_log):
        client = Client()
        response = client.get('/check_500/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '500.html')
        mock_sentry_log.assert_called_once_with(
            error_type='error',
            error_message='500 error. URL : /check_500/, Méthode : GET, Adresse IP : 127.0.0.1'
        )


class Error404ViewTests(TestCase):
    """
    Tests pour la vue d'erreur 404.

    Ces tests vérifient que la page d'erreur 404 est affichée correctement
    lorsque le mode DEBUG est désactivé.
    """
    @patch('oc_lettings_site.views.sentry_log')
    @override_settings(DEBUG=False)
    def test_error404_view(self, mock_sentry_log):
        """
        Test de la vue d'erreur 404.

        Ce test envoie une requête GET à une URL inexistante et vérifie que le
        code de statut HTTP est 200 (même en cas d'erreur). Il vérifie également
        que le modèle de template utilisé est '404.html'.
        """
        client = Client()
        response = client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '404.html')


class SentryLogTests(TestCase):

    @patch('logging.exception')
    def test_logging_exception(self, mock_logging_exception):
        # Appeler la fonction avec le type d'erreur "exception"
        sentry_log(error_type="exception", error_message="Test Exception Message")

        # Vérifier que logging.exception a été appelé avec le bon message
        mock_logging_exception.assert_called_once_with("Test Exception Message")
