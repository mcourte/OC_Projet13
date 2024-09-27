Déploiement
===========

Qu'est-ce que le déploiement et CircleCI ?
------------------------------------------
Le déploiement est le processus par lequel une application est mise en production, rendant son utilisation possible pour les utilisateurs finaux. CircleCI est un service d'intégration et de déploiement continus (CI/CD) qui automatise les processus de test et de déploiement d'applications. Il permet de s'assurer que le code est de haute qualité avant d'être déployé en production.

Avantages de l'intégration continue avec CircleCI :
----------------------------------------------------
- **Automatisation** : CircleCI automatise le processus de test et de déploiement, réduisant ainsi le risque d'erreurs humaines.
- **Rapidité** : Les modifications apportées au code sont testées et déployées rapidement, ce qui permet une mise à jour continue des fonctionnalités et des corrections de bugs.
- **Qualité du code** : CircleCI exécute des tests automatisés et des analyses de linting, garantissant que seul le code de qualité est déployé.

Processus de déploiement avec CircleCI :
-----------------------------------------
1. **Configuration du projet** : Après avoir cloné le projet et configuré un environnement virtuel, créez un nouveau projet sur CircleCI lié à votre dépôt GitHub.
2. **Définition des variables d'environnement** : Configurez des variables d'environnement nécessaires à l'application dans CircleCI, telles que ALLOWED_HOSTS, DEBUG, DOCKERHUB_PASSWORD, et autres clés secrètes.
3. **Pipeline automatisé** : Lorsque des mises à jour sont poussées sur la branche master, CircleCI déclenche automatiquement le pipeline qui exécute les tests et le linting du code.
4. **Construction et déploiement** : Si les tests réussissent, CircleCI construit une image Docker et la pousse sur DockerHub. Ensuite, il déploie l'application sur Render.
5. **Surveillance et alertes** : CircleCI peut être intégré avec des outils comme Sentry pour surveiller les erreurs et recevoir des alertes en temps réel.


Le déploiement automatisé avec CircleCI permet d'améliorer l'efficacité, la rapidité et la qualité des mises à jour de l'application. En intégrant des tests automatisés et des vérifications de code, il contribue à maintenir une base de code robuste et fiable, tout en assurant une expérience utilisateur fluide et sans interruption.

1. Prérequis
------------
Pour effectuer le déploiement et l'intégration continue de l'application, les comptes suivants sont nécessaires :

- Compte GitHub
- Compte CircleCI (lié au compte GitHub)
- Compte Docker
- Compte Render
- Compte Sentry

2. Principe
-----------
Le déploiement de l'application est automatisé par le pipeline CircleCI. Lorsque des mises à jour sont poussées sur le dépôt GitHub, le pipeline déclenche l'exécution de la suite de tests et le linting du code pour toutes les branches du projet. Si des mises à jour sont effectuées sur la branche main, et uniquement si les tests et le linting réussissent.

Workflow :
- Construit une image Docker et la pousse sur DockerHub.
- Si l'étape précédente réussit, déploie l'application sur Render.

3. Configuration de CircleCI
----------------------------
1. Après avoir cloné le projet, configuré l'environnement virtuel local (voir section Développement local) et créé les comptes nécessaires, suivez ces étapes pour configurer un nouveau projet sur CircleCI :
2. Connectez-vous à votre compte CircleCI.
3. Allez sur "Projects" et sélectionnez "Set Up Project" pour le projet cloné depuis GitHub.
4. Choisissez la branche main comme source pour le fichier .circleci/config.yml.
5. Pour que le pipeline CircleCI fonctionne correctement, configurez les variables d'environnement suivantes (Paramètres du projet > Variables d'environnement) :
   
   - **ALLOWED_HOSTS** : Spécifiez les hôtes autorisés pour l'application (par exemple, localhost, your-domain.com).
   - **DEBUG** : Choisissez True (en local) ou False (en production).
   - **DOCKERHUB_PASSWORD** : Mot de passe du compte Docker.
   - **DOCKERHUB_USERNAME** : Nom d'utilisateur du compte Docker.
   - **HOOK_RENDER** : URL de l'API Render pour le déploiement automatique.
   - **SECRET_KEY** : Clé secrète de l'application Django (générée lors de la création du projet Django).
   - **SENTRY_DSN** : URL du projet Sentry pour le suivi des erreurs.
  
6. Ajout de tests et étapes supplémentaires : Vous pouvez personnaliser davantage le pipeline CircleCI en ajoutant des étapes de tests automatisés pour garantir la qualité du code avant le déploiement. Par exemple, vous pouvez ajouter des étapes pour :
   - Exécuter des tests unitaires avec pytest ou unittest.
   - Vérifier la qualité du code avec des outils comme flake8 pour le linting Python.
   - Mettre en cache les dépendances pour réduire le temps d'exécution.
7. Gestion des erreurs : Utilisez des outils tels que Sentry pour capturer les erreurs en temps réel dans l'application, et CircleCI peut intégrer ces alertes dans le pipeline.

8. Configuration de Render
--------------------------
1. Connectez-vous à votre compte Render.
2. Créez un Web Service pour l'application en spécifiant le dépôt GitHub où le code est hébergé.
3. Dans l'interface de Render, définissez les variables d'environnement requises pour votre application dans la section des paramètres du service Web :
   
   - **ALLOWED_HOSTS** : Saisissez les hôtes autorisés (comme your-domain.com ou localhost).
   - **DEBUG** : Choisissez True pour activer le mode debug ou False pour la production.
   - **DOCKERHUB_PASSWORD** : Mot de passe du compte Docker.
   - **DOCKERHUB_USERNAME** : Nom d'utilisateur du compte Docker.
   - **SECRET_KEY** : Clé secrète de Django pour votre application.
   - **SENTRY_DSN** : URL du projet Sentry pour le suivi des erreurs.
  
4. Hooks de déploiement : Configurez un webhook dans Render pour que CircleCI puisse déclencher automatiquement le déploiement une fois l'image Docker mise à jour sur DockerHub. Cela assure une continuité de l'intégration/déploiement en cas de succès des tests sur CircleCI.

Surveillance et logs : Render offre également des options pour surveiller votre application déployée, accéder aux logs, et vérifier la santé du service en continu.
