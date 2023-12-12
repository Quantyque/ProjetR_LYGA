# C1_ProjetR_LYGA

## Description du projet

Ce projet a été réalisé dans le cadre de la Saé du semestre 5 de BUT3 informatique à l'IUT de Dijon-Auxerre.

Ce projet est la partie back-end du projet R qui est un outil permettant d’établir un classement d’une communauté de jeu de combat. Il permet de gérer les utilisateurs, les personnages, les matchs et les tournois. Il permet aussi de générer des statistiques sur les personnages et les utilisateurs. 

## Installation

L'application possède une architécture client/serveur.
Nous vous invitons à regarder les "README.md" des répertoires "Client" et "Server" pour plus d'informations.
En effet, pour que l'application soit complète, il faut lançer le serveur et le client.

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

Ce fichier doit également contenir les informations pour définir les tokens d'identification utilisés pour sécuriser l'API et authentifier les utilisateurs.
Pour cela, contacter un membre du projet afin de l'obtenir ou utilisez un générateur de chaîne de caractère (doit être longue) avec des caractères complexes.

```bash
JWT_SECRET = <secret>
JWT_ALGO = HS256
```

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

Le projet est composé de trois dossier principaux :

- **Client** : contient la partie cliente de l'application
- **Server** : contient la partie serveur de l'application
- **Conception** :  contient le fichier de conception du projet

## Auteurs

Ce projet a été réalisé par :
* Grégory Yontchev
* Lucas Pupat
* Youri Emmanuel
* Antoine Richard

## Licence

Ce projet appartient à l'IUT Dijon-Auxerre car ayant été réalisé dans le cadre d'un projet de Saé du semestre 5 de BUT3 informatique.