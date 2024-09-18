from django.test import TestCase, override_settings, Client
from django.urls import reverse


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
    Tests pour la vue d'erreur 500.

    Ces tests vérifient que la page d'erreur 500 est affichée correctement
    lorsque le mode DEBUG est désactivé.
    """

    @override_settings(DEBUG=False)
    def test_error500_view(self):
        """
        Test de la vue d'erreur 500.

        Ce test envoie une requête GET à une URL qui provoque une erreur 500
        et vérifie que le code de statut HTTP est 200 (même en cas d'erreur).
        Il vérifie également que le modèle de template utilisé est '500.html'.
        """
        client = Client()
        response = client.get('/check_500/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '500.html')


class Error404ViewTests(TestCase):
    """
    Tests pour la vue d'erreur 404.

    Ces tests vérifient que la page d'erreur 404 est affichée correctement
    lorsque le mode DEBUG est désactivé.
    """

    @override_settings(DEBUG=False)
    def test_error404_view(self):
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
