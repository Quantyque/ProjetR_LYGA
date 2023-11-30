# C1_ProjetR_LYGA

## Description du projet

Ce projet a été réalisé dans le cadre de la Saé du semestre 5 de BUT3 informatique à l'IUT de Dijon-Auxerre.

Ce projet est la partie back-end du projet R qui est un outil permettant d’établir un classement d’une communauté de jeu de combat. Il permet de gérer les utilisateurs, les personnages, les matchs et les tournois. Il permet aussi de générer des statistiques sur les personnages et les utilisateurs. 

## Installation

L'application possède une architecture client/serveur. Vous êtes ici sur la partie serveur/API
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

Vous pouvez ensuite lancer le projet (serveur) avec la commande suivante : 

```bash
python main.py
```

## Utilisation

Pour utiliser le projet, il faut utiliser l’API. Pour cela, il faut utiliser un client (logiciel) comme Postman ou Insomnia ou l'application Client.
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

- **constants** : contient les constantes du projet
- **controls** : contient les contrôles qui permettent de vérifier les données envoyées par l’utilisateur
- **data_processing** : contient les classes de la base de données
- **exceptions** : contient les exceptions du projet
- **logs** : contient les logs du projet où sont stockées les erreurs
- **manager** : contient les managers qui permettent de gérer les objets de la base de données et de l'api start.gg
- **model** : contient les modèles qui permettent de représenter les objets de la base de données et de l'api start.gg
- **unit_tests** : contient les tests unitaires du projet
- **utils** : contient les fonctions utilitaires du projet
- **views** : contient les controllers du projet qui font le lien entre les routes et les managers
- **main.py** : contient les routes du projet

## Routes

Retrouvez ci-dessous les divers services alloués par l'API.
**/!\ Les services nécessitant une permission doivent accorder un token d'authentification dans l'entête "Authorization" des requêtes qui leur seront adressés sous format "Bearer $token" /!\**
Les échanges s'effectuent en JSON.

### Video Games

|            **Route**             |                 **Description**                 |    **Require**    | **Permission** | **HTTP Protocol** |
| :------------------------------: | :---------------------------------------------: | :---------------: | :------------: | :---------------: |
|      {host}/videogames/all       | Récupère tous les jeux disponibles sur Start.gg |       None        |      None      |        GET        |
|    {host}/videogames/audited     | Récupère la liste des jeux audités enregistrés  |       None        |      None      |        GET        |
|  {host}/videogames/add-audited   |   Ajout d'un jeu à la liste des jeux audités    | id: int name: str |     ADMIN      |       POST        |
| {host}/videogames/update-audited |  Modifie un jeu dans la liste des jeux audités  | id: int name: str |     ADMIN      |        PUT        |
| {host}/videogames/delete-audited |  Supprime un jeu de la liste des jeux audités   |      id: int      |     ADMIN      |      DELETE       |

### Player

|        **Route**         |                                            **Description**                                             |           **Require**            | **Permission** | **HTTP Protocol** |
| :----------------------: | :----------------------------------------------------------------------------------------------------: | :------------------------------: | :------------: | :---------------: |
|    {host}/player/all     |                       Renvoi la liste de tous les joueurs de la base de données                        |               None               |      None      |        GET        |
|   {host}/player/infos    |                       Renvoi les informations d'un joueur en fonction de son id                        |          player_id: int          |      None      |       POST        |
| {host}/player/all_ranked | Renvoi la liste des joueurs classés par elo pour un jeu donné ayant joué le nombre de tournois minimum | videogame_id: int season_id: int |      None      |       POST        |

### Ranking

|                **Route**                |                                             **Description**                                              |                          **Require**                          | **Permission** | **HTTP Protocol** |
| :-------------------------------------: | :------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------: | :------------: | :---------------: |
|         {host}/rankings/update          | Met à jour le classement des joueurs en fonction des tounoirs passés depuis une date donnée manuellement | date: datetime videogameId: int cordonnees: str distance: str |     ADMIN      |       POST        |
| {host}/rankings/parameters/auto-refresh |           Rafraichit automatiquement le classement des joueurs en fonction des tournois passés           |                        activate: bool                         |     ADMIN      |        PUT        |

### Tournaments

|          **Route**          |                  **Description**                   |                                  **Require**                                   | **Permission** | **HTTP Protocol** |
| :-------------------------: | :------------------------------------------------: | :----------------------------------------------------------------------------: | :------------: | :---------------: |
| {host}/tournaments/location | Renvoi une liste de tournois par date, jeu et lieu | afterDate: str beforeDate: str videoGameId: int cordonnees: dict distance: int |      None      |       POST        |

### Users

|       **Route**       |                **Description**                |                             **Require**                              | **Permission** | **HTTP Protocol** |
| :-------------------: | :-------------------------------------------: | :------------------------------------------------------------------: | :------------: | :---------------: |
| {host}/user/register  | Ajoute un utilisateur dans la base de données |          username: str password: str confirm_password: str           |      None      |       POST        |
|   {host}/user/login   |    Connecte un utilisateur à l'application    |                     username: str password: str                      |      None      |       POST        |
|  {host}/user/get-all  |        Retourne tous les utilisaeteurs        |                                 None                                 |      None      |        GET        |
| {host}/user/get-by-id | Retourne un utilisateur en fonction de son id |                               id: int                                |      None      |       POST        |
|  {host}/user/update   |          Met à jour à l'utilisateur           | id: int username: str password: str (optional) userPP: str role: int | Connected user |        PUT        |
|  {host}/user/delete   |            Supprime un utilisateur            |                               id: int                                | Connected user |      DELETE       |

### Set

|      **Route**      |            **Description**            | **Require** | **Permission** | **HTTP Protocol** |
| :-----------------: | :-----------------------------------: | :---------: | :------------: | :---------------: |
| {host}/sets/player/ | Renvoie les derniers sets d'un joueur | player: int |      None      |       POST        |

### Elo

|         **Route**         |                                  **Description**                                  |                 **Require**                 | **Permission** | **HTTP Protocol** |
| :-----------------------: | :-------------------------------------------------------------------------------: | :-----------------------------------------: | :------------: | :---------------: |
|    {host}/elo/default     | Renvoi l'elo par défaut d'un joueur en fonction de son id et de l'id du jeu vidéo |         player_id: int videogame_id         |      None      |       POST        |
|  {host}/elo/add-default   |                       Ajoute un elo par défaut à un joueur                        | player_id: int videogame_id: int score: int |     ADMIN      |       POST        |
|  {host}/elo/edit-default  |                             Modifie l'elo d'un joueur                             |  player_id: int videogame_id: int elo: int  |     ADMIN      |       POST        |
| {host}/elo/delete-default |                       Supprime l'élo par défaut d'un joueur                       |       player_id: id videogame_id: id        |     ADMIN      |      DELETE       |
|  {host}/elo/get-history   |                     Renvoi l'historique des elos d'un joueur                      |               player_id: int                |      None      |       POST        |

### Tests

|    **Route**     |           **Description**            | **Require** | **Permission** | **HTTP Protocol** |
| :--------------: | :----------------------------------: | :---------: | :------------: | :---------------: |
| {host}/tests/run | Exécute les tests unitaires de l'API |    None     |     ADMIN      |        GET        |

### Season

|      **Route**       |             **Description**             |                            **Require**                             | **Permission** | **HTTP Protocol** |
| :------------------: | :-------------------------------------: | :----------------------------------------------------------------: | :------------: | :---------------: |
|  {host}/season/get   | Renvoi une saison en fonction de son id |                           season_id: int                           |      None      |       POST        |
|  {host}/season/all   |        Renvoi toutes les saisons        |                                None                                |      None      |        GET        |
|  {host}/season/add   |            Ajoute une saison            |        number: int start_date: datetime end_date: datetime         |     ADMIN      |       POST        |
| {host}/season/update |          Met à jour la session          | season_id: int number: int start_date: datetime end_date: datetime |     ADMIN      |        PUT        |
| {host}/season/remove |           Supprime une saison           |                           season_id: int                           |     ADMIN      |      DELETE       |

## Auteurs

Ce projet a été réalisé par :
* Grégory Yontchev
* Lucas Pupat
* Youri Emmanuel
* Antoine Richard

## Licence

Ce projet appartient à l'IUT Dijon-Auxerre car ayant été réalisé dans le cadre d'un projet de Saé du semestre 5 de BUT3 informatique.