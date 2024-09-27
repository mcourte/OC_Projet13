Contexte
========

1. Spécifications
-----------------

- `App specifications <https://github.com/canofranck/P13_OC_-Lettings_FR/blob/main/specifications/Site_web_2_0_caractéristiques_et_améliorations.pdf>`_ 
- `Doc specifications <https://github.com/canofranck/P13_OC_-Lettings_FR/blob/main/specifications/Configuration_Read_the_Docs.pdf>`_ 

2. Description du projet
------------------------

   Refonte de l'architecture modulaire dans le `GitHub repository <https://github.com/NidalChateur/OC_P13_LETTINGS>`_  

      1. Résolution de diverses dettes techniques dans le projet.

      2. `Dockersation <https://hub.docker.com/repository/docker/mcourte/my-app/general>`_  

      3. Mise en place d'un pipeline CI/CD en utilisant `CircleCI <https://app.circleci.com/pipelines/circleci/Y8j2gRnHZve8of2ZKg9fsg>`_ et déploiement sur `Render <https://dashboard.render.com/>`_  

      4. Surveillance de l'application et suivi des erreurs via `Sentry <https://sentry.io>`_  

      5. Création de la documentation technique de l'application avec  `Read The Docs <https://about.readthedocs.com/>`_ et `Sphinx <https://github.com/sphinx-doc/sphinx>`_  


3. Configuration du système
---------------------------

- Linux Mint
- Visual Studio Code 1.93.1
- Python 3.12.0
- pip 24.2

4. Packages de développement
----------------------------


Pendant le développement local, nous utilisons  **.venv**

- django 5.0.8
   - **SECRET_KEY** : Django secret key
   - **SENTRY_DSN** : Sentry project URL
   - **ALLOWED_HOSTS** : enter allowed host 
   - **DEBUG** : select True or False
   - **DOCKERHUB_PASSWORD** : Docker account password
   - **DOCKERHUB_USERNAME** : Docker account username
   - **HOOK_RENDER** (acquired from Render)

5. Package de tests
-------------------

- pytest 8.3.2
- pytest-cov 5.0.0
- pytest-django 4.8.0
- flake8 7.1.1
- flake8-html 0.4.3

Pour la couverture de test utilisez : 
   .. code-block:: console

      $ pytest --cov=. --cov-report=html

1. Production packages
----------------------

   - gunicorn 23.0.0
   - whitenoise 6.7.0
   - sentry-sdk 2.14.0


7. Modèles de Base de Données
-----------------------------

.. py:class:: class Address(models.Model):

   - number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
   - street = models.CharField(max_length=64)
   - city = models.CharField(max_length=64)
   - state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
   - zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
   - country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])


.. py:class:: class Letting(models.Model):

   - title = models.CharField(max_length=256)
   - address = models.OneToOneField(Address, on_delete=models.CASCADE)


.. py:class:: class Profile(models.Model):
   
   - user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profiles_profile')
   - favorite_city = models.CharField(max_length=64, blank=True)


