.. OC-Lettings-Site documentation master file, created by
   sphinx-quickstart on Thu Sep 26 16:07:46 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Installation
============

Cette section explique comment installer l'application.

Pré-requis
----------

- Python 3.12
- pip

Étapes d'installation
---------------------

Etape 1 : Télécharger le code
------------------------------
Vous pouvez cloner le dépôt git dans lequel se trouve l'ensemble du projet :  
Placez-vous dans le dossier dans lequel vous souhaitez cloner le dépôt et tapez :

   .. code-block:: console

      $ git clone https://github.com/mcourte/OC_Projet13.git

Etape 2 : Installer Python et ouvrir le terminal de commande
------------------------------------------------------------

Téléchargez `Python <https://www.python.org/downloads/>`_ et `installez-le <https://fr.wikihow.com/installer-Python>`_.

Ouvrez le terminal de commande :  
Pour les utilisateurs de Windows : `procédure à suivre <https://support.kaspersky.com/fr/common/windows/14637#block0>`_  
Pour les utilisateurs de Mac OS : `démarche à suivre <https://support.apple.com/fr-fr/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac>`_  
Pour les utilisateurs de Linux : ouvrez directement le terminal de commande.

Etape 3 : Création de l'environnement virtuel
----------------------------------------------

Placez-vous dans le dossier où l'on a extrait l'ensemble des documents grâce à la commande ``cd``.  
Exemple :

   .. code-block:: console

      $ cd /home/magali/OpenClassrooms/Formation/Projet_13

Dans le terminal de commande, exécutez la commande suivante :

   .. code-block:: console

      $ python3 -m venv venv

Activez l'environnement virtuel :

   .. code-block:: console

      $ source venv/bin/activate

Pour les utilisateurs de Windows, la commande est la suivante :

   .. code-block:: console

      $ venv\Scripts\activate.bat

Etape 4 : Télécharger les packages nécessaires au bon fonctionnement du programme
---------------------------------------------------------------------------------

Installez ensuite les packages requis :

   .. code-block:: console

      $ pip install -r requirements.txt

