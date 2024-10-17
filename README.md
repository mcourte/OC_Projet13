
# Projet 12 : Développez une architecture back-end sécurisée avec Python et SQL


## Accéder au projet et le mettre en route
Pour savoir comment utiliser l'application, liser la [Documentation ReadTheDocs](https://oc-projet13.readthedocs.io/fr/latest/)



Améliorations du site **OC Lettings**  à partir du projet
[Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR) :


## Etape 1 : Réduction de la dette technique

   - Corriger les erreurs de linting
   - Corriger la pluralisation des noms de modèles dans le site d'administration


## Etape 2 : Refonte de l'architecture modulaire

   - Créer 3 applications *lettings*, *profiles* et *Oc_lettings_site* pour séparer les fonctionnalités de l'application
   - Développer une suite de tests


## Etape 3:  Ajout d'un pipeline CI/CD avec [CircleCI](https://circleci.com) et déploiement sur [Render](https://render.com/)

   1) *Compilation* : exécuter le linting et la suite de tests 
   2) *Conteneurisation* : construire et push une image du site avec [Docker](https://www.docker.com) 
   3) *Déploiement* : mettre en service le site avec Render 
   4) Surveillance de l'application et suivi des erreurs via [Sentry](https://sentry.io/welcome/)

### Liens rapides :
- **[Pipeline CircleCI de ce projet](https://app.circleci.com/pipelines/circleci/BETbtxagzTyRzvxKtbzjdS/8EfgRimj6nw7PPABmwB4Cq)**
- **[Images Docker disponibles](https://hub.docker.com/r/mcourte/my-app)**
- **[Application déployée sur Render](https://oc-projet13-kqrq.onrender.com)**
