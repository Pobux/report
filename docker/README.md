Tuto
====
Installation : https://linuxconfig.org/how-to-install-docker-on-ubuntu-18-04-bionic-beaver
Docker swarm : https://sysadmins.co.za/setup-a-3-node-docker-swarm-on-ubuntu-16/
Docker machine (gestion des hosts) : https://docs.docker.com/machine/install-machine/#install-machine-directly

Docker
======
Les images sont de python-alpine (image plus lègère)

Pour lancer docker swarm (Voir swarm avant afin de créer le réseau correctement)
docker stack deploy --compose-file flask-app.yml apps --with-registry-auth

Swarm
=====
Un docker swarm est composé de deux types de noeuds:
1. Manager : Peut rouler un service mais sert principalement à coordonner le quorum des machines. Il dit aux workers ce qu'ils doivent faire

2. Worker

Le fichier host définit les adresses sur lesquels les microservices communiqueront (manager et worker)
Basé sur le host file hosts.sample (cat hosts.sample >> /etc/hosts)
