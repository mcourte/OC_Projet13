.. OC-Lettings-Site documentation master file, created by
   sphinx-quickstart on Thu Sep 26 16:07:46 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
OC-Lettings-Site documentation
==========

.. contents::
   :depth: 2
   :local:

Introduction
------------

Bienvenue dans la documentation de mon projet. Ce document vous guidera à travers les étapes d'installation, d'utilisation de Docker, et de déploiement.

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
-----------------------------
Cliquer sur le bouton vert "<> Code" puis sur Download ZIP.  
Extraire l'ensemble des éléments dans le dossier dans lequel vous voulez stockez les datas qui seront téléchargées.
Vous pouvez également cloner le dépôt:  
Placer vous dans la dossier dans lequel vous souhaitez cloner le git et taper ``git clone https://github.com/mcourte/OC_Projet13.git``


Etape 2 ; Installer Python et ouvrir le terminal de commande
------------------------------------------------------------

Télécharger [Python] (https://www.python.org/downloads/) et [installer-le] (https://fr.wikihow.com/installer-Python)

Ouvrir le terminal de commande :  
Pour les utilisateurs de Windows : [démarche à suivre] (https://support.kaspersky.com/fr/common/windows/14637#block0)  
Pour les utilisateurs de Mac OS : [démarche à suivre] (https://support.apple.com/fr-fr/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)  
Pour les utilisateurs de Linux : ouvrez directement le terminal de commande   


Etape 3 : Création de l'environnement virtuel
---------------------------------------------
Se placer dans le dossier où l'on a extrait l'ensemble des documents grâce à la commande ``cd``  
Exemple :
``cd home/magali/OpenClassrooms/Formation/Projet_13``


Dans le terminal de commande, executer la commande suivante :
``python3 -m venv venv``


Activez l'environnement virtuel
``source venv/bin/activate``
- Pour les utilisateurs de Windows, la commande est la suivante : 
-  ``venv\Scripts\activate.bat``

Etape 4 : Télécharger les packages nécessaires au bon fonctionnement du programme
--------------------------------------------------------------------------------

Installez ensuite les packages requis:  
``pip install -r requirements.txt``



.. toctree::
   :maxdepth: 2
   :caption: Contents:

