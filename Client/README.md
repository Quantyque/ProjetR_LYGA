# C1_ProjetR_LYGA

## Description du projet

Ce projet a été réalisé dans le cadre de la Saé du semestre 5 de BUT3 informatique à l'IUT de Dijon-Auxerre.

Ce projet est la partie back-end du projet R qui est un outil permettant d’établir un classement d’une communauté de jeu de combat. Il permet de gérer les utilisateurs, les personnages, les matchs et les tournois. Il permet aussi de générer des statistiques sur les personnages et les utilisateurs. 

## Installation

L'application possède une architécture client/serveur.
Pour installer le projet, il faut cloner le projet sur votre machine. 
Ensuite, il faut installer les dépendances du projet avec la commande suivante : 

```bash
pip install -r requirements.txt
```

Pour utiliser le projet, il faut créer une clé API sur le site start.gg. 
Il faut ensuite créer un fichier .env à la racine du projet avec la clé API. 
Le fichier doit contenir la ligne suivante : 

```bash
STARTGG_KEY = <clé_api>
```

Ce fichier foit également contenir les informations pour obtenir le hachable du mot de passe.
Pour cela, contacter un membre du projet afin de l'obtenir.

Vous pouvez ensuite lancer le projet avec la commande suivante : 

```bash
python main.py
```

Pour obtenir le site sur une page internet, il faut faire la commande qui suit :

```bash
npm run dev
```

Ensuite, selon l'adresse du serveur que vous avez choisie, il vous suffiras de cliquer sur le lien.

Si ça ne fonctionne pas, vous pouvez utiliser la commande ci-dessous pour mettre à jour les dépendances du projet :

```bash
npm i
```

## Utilisation

Pour utiliser le projet, il faut utiliser l’API. Pour cela, il faut utiliser un logiciel comme Postman.
Les routes disponibles sont decrites dans le fichier main.py.

Par exemple, pour récupérer les informations d'un joueur, il faut utiliser la route suivante : 

```bash
http://<nom_server>/player/infos
```

Avec la méthode POST et le body suivant : 

```bash
{
    "player_id": <id_joueur>
}
```

## Structure du projet

Le projet est composé de plusieurs dossiers :

- **app** : contients les pages de l'application, l'authentification à l'API et les composantes des pages
- **controller** : contient les controleurs des types de données. C'est ce qui permet de faire la passerelle entre la vue et le model
- **public** : contient les fichiers publiques qu'utilise l'application.

## Routes

L'application utilise le framework Next.js. Le framework impose les racines par nom de répertoire dans le dossier "app/(pages)/(main)" et seulement les fichiers ayant comme nom "page.tsx" sont éxécutés en tant que page.
Par exemple, si un dossier dans "(main)" se nomme "home", l'url est alors "http://localhost:3000/home" et le dossier doit avoir un fichier s'appelant "page.tsx".
Le framework permet aussi d'utiliser des comosants à des pages. Cela permet d'afficher des éléments qui sont amenés à changer sur une même page, par exemple.

## Auteurs

Ce projet a été réalisé par :
* Grégory Yontchev
* Lucas Pupat
* Youri Emmanuel
* Antoine Richard

## Licence

Ce projet appartient à l'IUT Dijon-Auxerre car ayant été réalisé dans le cadre d'un projet de Saé du semestre 5 de BUT3 informatique.