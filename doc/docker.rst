Docker
=========

Qu'est-ce que Docker et à quoi sert-il ?
----------------------------------------

Docker est un outil permettant de créer, déployer et exécuter des applications dans des "conteneurs". Un conteneur est une sorte d'enveloppe virtuelle qui regroupe tout ce dont une application a besoin pour fonctionner (code, bibliothèques, dépendances, etc.). Cela permet de s'assurer que l'application fonctionne de la même manière, que ce soit sur votre machine locale, sur un serveur ou dans le cloud.

Les principaux avantages de Docker sont :

1. **Portabilité** : Une application Dockerisée peut être exécutée sur n'importe quel système qui prend en charge Docker, sans avoir à se soucier des différences de configuration.
2. **Isolation** : Chaque conteneur fonctionne de manière indépendante des autres, ce qui réduit les risques de conflits entre applications.
3. **Efficacité** : Contrairement aux machines virtuelles, les conteneurs utilisent les ressources de manière plus efficace, car ils partagent le noyau du système hôte.

Créer une image Docker pour exécuter l'application en local
-----------------------------------------------------------

1. **Télécharger et installer Docker** :

   Suivez les instructions de la documentation officielle pour installer Docker :  
   `Docker Installation <https://docs.docker.com/get-started/get-docker/>`_.

2. **Naviguer dans le répertoire du projet** :  

   Ouvrez un terminal et exécutez la commande suivante pour vous rendre dans le dossier du projet :

   .. code-block:: console

      $ cd /home/magali/OpenClassrooms/Formation/Projet_13

3. **Assurez-vous que l'environnement virtuel (.venv) a été préalablement créé** :

   Avant de continuer, vérifiez que l'environnement virtuel a été configuré (voir la section Installation).


Utiliser une image existante depuis DockerHub pour exécuter l'application en local
-----------------------------------------------------------------------------------

1. **Télécharger et installer Docker** :

   Suivez les instructions de la documentation officielle pour installer Docker :  
   `Docker Installation <https://docs.docker.com/get-started/get-docker/>`_.

2. **Accéder au dépôt DockerHub** :

   Allez sur le dépôt DockerHub à l'adresse suivante :  
   `mcourte/my-app`.  
   Ce dépôt contient des images pré-construites de l'application.

3. **Choisir une version (tag)** :

   Copiez le tag de la version que vous souhaitez utiliser. Il est recommandé de choisir la version la plus récente.

4. **Lancer l'application depuis DockerHub** :

   Utilisez la commande suivante pour exécuter l'application directement depuis DockerHub. Remplacez `<tag>` par le tag que vous avez copié à l'étape précédente :

   .. code-block:: console

      $ docker run --rm -p 8000:8000 mcourte/my-app

5. **Accéder à l'application** :

   Comme précédemment, ouvrez un navigateur et accédez à l'application à l'adresse  
   `http://127.0.0.1:8000/`.

Résumé
------

- **Docker image** : Une image est une sorte de "photo" figée de votre application avec toutes ses dépendances.
- **docker build** : Cette commande crée une image Docker à partir de votre projet local.
- **docker run** : Cette commande exécute une image Docker. Vous pouvez soit exécuter une image que vous avez construite, soit en télécharger une déjà prête sur DockerHub.

Docker permet donc de facilement tester et déployer des applications en local ou sur des serveurs, tout en garantissant que l’environnement d’exécution est identique partout.
