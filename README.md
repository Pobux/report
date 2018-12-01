Requis
======

Installation python3
--------------------
- Avoir `virtualenv` 
    - Créer l'environnement virtuel sous `report`, `virtualenv -p python3 venv`
    - Entrer dans l'environnement virtuel, `source venv/bin/activate`
    - Installer les dépendances `pip install -r requirements.txt`

À noter que chaque service possède ses propres dépendances de librairies et que le développement pour chacun d'entre eux se fait par le démarrage d'un environnement virtuel.

Installation docker
-------------------
- Suivre la documentation de docker qui est très bien faite selon votre OS.
- Installer docker-compose

Indépendance des services
-------------------------
L'indépendance des services implique :
- Que chacun des services doit avoir son propre Dockerfile (ça recette)
- Son propre fichier `requirements.txt` 
- Que docker-compose `links` les services ensemble

Construire les services
=======================
Sous `./docker` lancer `sudo docker-compose up --force-recreate --build`

Les services devraient démarrés sans erreur.

À noter que le service log dépend d'une connexion ouverte vers le service de rabbitmq. Celui tentera une connexion jusqu'à ce que celle-ci fonctionne.

Tester directement la gateway
=============================
Dans le navigateur, seulement tapper l'adresse suivante afin de voir si l'ensemble des service fonctionne

"0.0.0.0:5000/log"

Client side
===========
Uses vue.js

Vue installation
----------------
router - yes

ESLint - yes

ESLint preset - standard

Mocha - no

Nightwatch - no
