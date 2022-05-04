# Welfare

## Description

Ce projet à pour but de poser des questions vis à vis du bien-être en entreprise et enregistrer le tout dans une base de donnée.
L'utilisateur pourra ainsi s'enregistrer et répondre de manière anonyme aux différentes questions.

## Prérequis

- docker >= 20.10.12
- python >= 3.10.2

## Docker

Docker est une application nous permettant de conteneriser notre application. Ansi, vous pourrez faire tourner cette application en local sur le port 9000.

Ouvrir un terminal à la base de notre projet, lancez la commande :

$ docker-compose up -d

Tapez dans la barre de recher de votre navigateur http://localhost:9000s
Installation de Docker sur Windows :
$ curl https://desktop-stage.docker.com/linux/main/amd64/77103/docker-desktop.deb --output docker-desktop.deb
$ sudo apt install ./docker-desktop.deb

Installation de Docker sur Mac :
Rendez vous sur le site afin d'installer le Docker Desktop: https://docs.docker.com/desktop/mac/install/
## Kubernetes:

Pour faire ds nodes avec Kubernetes vous pouvez utiliser Minikube et utiliser le kubernetes dashboard, vous pouvez suivre les étapes suivantes:
$ brew install minikube (pour mac os)
$ minikube start
$ minikube tunnel (laisser le tunnel tourner)
ouvrir un nouveau terminal

$ kubectl apply -f .
$ minikube dashboard
localhost:9000 (dans la barre de recherche)

Sinon vous pouvez utiliser kubernetes directement dans votre docker dashboard qui s'occupera de faire vos nodes à la place de Minikube. Cette opération est plus facile et plus fiable.

Cependant, vous devez utiliser un dashboard afin de visualiser vos opérations.

Vous avez une large liste de dashboard, ici nous avons utilisé Octant.

Installation d'Octant :

Sur linux il faut se rendre sur la page des releases du projet pour télécharger le package .deb ou .rpm. Par exemple pour l’installer sur une redhat family :

$ sudo dnf install wget https://github.com/vmware-tanzu/octant/releases/download/v0.25.0/octant_0.25.0_Linux-64bit.rpm

Sur MacOS un brew classique :

$ brew install octant

Puis dans le terminal à l'emplacement de votre projet, tapez octant pour ouvrir votre Dashboard.
## Terraform Azure:

Il y'a plusieurs manières d'utiliser terraform pour déployer une application dans le cloud, nous on a choisi docker.

N.B: avant de commencer l'écriture du fichier terraform, préparer votre image docker et l'envoyer dans votre docker hub.

Au début du fichier indique qu'on va utiliser terraform.
Dire à terraform qu'on va utiliser le provider azurerm ( dans ce provider, penser à utiliser vos id de souscriptions azure. )

Créer un ressource groupe
Créer un app service plan
Créer un app service ( - a ce niveau dire au fichier qu'il va utiliser notre image docker -- n'oubliez pas de mettre ":latest" devant votre image. - lui indiquer l'url du docker hub hébergeant notre image. )
Faire un output pour récupérer l'url du site maintenant hébergé dans le cloud de azure.