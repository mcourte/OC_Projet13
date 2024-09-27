3. Déploiement
===================

1. Prérequis
------------
Pour effectuer le déploiement et l'intégration continue de l'application, les comptes suivants sont nécessaires :

- Compte GitHub
- Compte CircleCI (lié au compte GitHub)
- Compte Docker
- Compte Render
- Compte Sentry

1. Résumé
---------
Le déploiement de l'application est automatisé par le pipeline CircleCI. Lorsque des mises à jour sont poussées sur le dépôt GitHub, le pipeline déclenche l'exécution de la suite de tests et le linting du code pour toutes les branches du projet. Si des mises à jour sont effectuées sur la branche master, et uniquement si les tests et le linting réussissent, le workflow :

Construit une image Docker et la pousse sur DockerHub.
Si et seulement si l'étape précédente réussit, déploie l'application sur Render.

2. Configuration de CircleCI
----------------------------

1. Après avoir cloné le projet, configuré l'environnement virtuel local (voir section Développement local) et créé les comptes nécessaires, suivez ces étapes pour configurer un nouveau projet sur CircleCI :

2. Connectez-vous à votre compte CircleCI.

3. Allez sur "Projects" et sélectionnez "Set Up Project" pour le projet cloné depuis GitHub.

4. Choisissez la branche main comme source pour le fichier .circleci/config.yml.

5. Pour que le pipeline CircleCI fonctionne correctement, configurez les variables d'environnement suivantes (Paramètres du projet > Variables d'environnement) :

- ALLOWED_HOSTS : Spécifiez les hôtes autorisés pour l'application (par exemple, localhost, your-domain.com).
- DEBUG : Choisissez True (en local) ou False (en production).
- DOCKERHUB_PASSWORD : Mot de passe du compte Docker.
- DOCKERHUB_USERNAME : Nom d'utilisateur du compte Docker.
- HOOK_RENDER : URL de l'API Render pour le déploiement automatique.
- SECRET_KEY : Clé secrète de l'application Django (générée lors de la création du projet Django).
- SENTRY_DSN : URL du projet Sentry pour le suivi des erreurs.

6. Ajout de tests et étapes supplémentaires : Vous pouvez personnaliser davantage le pipeline CircleCI en ajoutant des étapes de tests automatisés pour garantir la qualité du code avant le déploiement. Par exemple, vous pouvez ajouter des étapes pour :

7. Exécuter des tests unitaires avec pytest ou unittest.
   
8. Vérifier la qualité du code avec des outils comme flake8 pour le linting Python.
   
9. Mettre en cache les dépendances pour réduire le temps d'exécution.

10. Gestion des erreurs : Utilisez des outils tels que Sentry pour capturer les erreurs en temps réel dans l'application, et CircleCI peut intégrer ces alertes dans le pipeline.

3. Configuration de Render
--------------------------
1. Connectez-vous à votre compte Render.

2. Créez un Web Service pour l'application en spécifiant le dépôt GitHub où le code est hébergé.

3. Dans l'interface de Render, définissez les variables d'environnement requises pour votre application dans la section des paramètres du service Web :

- ALLOWED_HOSTS : Saisissez les hôtes autorisés (comme your-domain.com ou localhost).
- DEBUG : Choisissez True pour activer le mode debug ou False pour la production.
- DOCKERHUB_PASSWORD : Mot de passe du compte Docker.
- DOCKERHUB_USERNAME : Nom d'utilisateur du compte Docker.
- SECRET_KEY : Clé secrète de Django pour votre application.
- SENTRY_DSN : URL du projet Sentry pour le suivi des erreurs.
- Hooks de déploiement : Configurez un webhook dans Render pour que CircleCI puisse déclencher automatiquement le déploiement une fois l'image Docker mise à jour sur DockerHub. Cela assure une continuité de l'intégration/déploiement en cas de succès des tests sur CircleCI.

Surveillance et logs : Render offre également des options pour surveiller votre application déployée, accéder aux logs, et vérifier la santé du service en continu.
