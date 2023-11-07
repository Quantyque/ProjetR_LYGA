from manager.manager import Manager
from model.player import Player
from model.elo import Elo
from model.videogame import Videogame
from constants import NUMBER_OF_TOURNAMENTS_TO_BE_RANKED

class PlayerManager(Manager):
    """
    Classe permettant de gérer les joueurs
    """

    def __init__(self):
        super().__init__()


    # region Operations

    def get_player_by_id(self, id : int) -> Player:
        """
        Récupère un joueur par son id
        """
        player : Player = Player()
        response = super().request_api("""
                query PlayerById($idPlayer : ID!) {
                    player(id: $idPlayer) {
                        id
                        prefix
                        gamerTag
                        user{
                            authorizations{
                            url
                            }  
                            images{
                            url
                            type
                            }
                            bio
                        }
                        sets(perPage: 25) {
                        nodes {
                            id
                            event{
                            videogame{
                                id,
                                name
                            }
                            }
                            games{
                                selections{
                                    entrant{
                                        standing{
                                            player{
                                                id
                                                gamerTag
                                            }
                                        }
                                    }
                                    character{
                                        id
                                        name
                                       images{
                                        url
                                       }
                                    }
                                }
                            }
                        }
                        }
                    }
                    }
                    """,
                    {"idPlayer" : id})
        player.hydrate(response["data"]["player"])

        #Récupération des elos depuis la base de données
        res = super().Database.exec_request("Select idElo, max(score), idPlayer, idGame, name, imageUrl from elos natural join games group by idPlayer having (idPlayer = ?)", (id,))
        for row in res:
            data_video_game = {
                "id": row[3],
                "name": row[4],
                "images": [{ "url" : row[5], "type" : "profile" }]
            }
            elo = Elo()
            dataElo = {
                "id": row[0],
                "score": row[1],
                "videogame": data_video_game
            }
            elo.hydrate(dataElo)
            player.Elos[row[3]] = elo
        
        return player
    
    def get_all_players(self) -> [Player]:
        """
        Récupère tous les joueurs de la base de données
        """
        players = {}
        res = super().Database.exec_request("""Select p.idPlayer, name, profilPicture, score, idGame, nbTournaments, prefix from players p natural join elos e join 
                (SELECT
            idPlayer,
            MAX(date) AS date_max FROM
            elos
        GROUP BY
            idPlayer) sub
			on e.idPlayer = sub.idPlayer
    AND e.date = sub.date_max""")
        for row in res:
            player : Player = Player()
            if not row[0] in players.keys():
                data_player = {
                    "id": row[0],
                    "gamerTag": row[1],
                    "user" : {
                        "images": [{ "url" : row[2], "type" : "profile" }]
                    },
                    "nbTournaments": row[5],
                    "prefix": row[6]
                }
                player.hydrate(data_player)
            else:
                player = players[row[0]]
            elo = Elo()
            data_elo = {
                "score": row[3],
                "videogame": {
                    "id": row[4]
                }
            }
            elo.hydrate(data_elo)
            player.Elos[row[4]] = elo
            players[row[0]] = player
        return players
    
    def get_ranked_players(self, videogame_id : int) -> [Player]:
        """
        Renvoie les joueurs classés par élo pour un jeu donné ayant fait le nombre de tournois minimum
        """
        players = {}
        res = super().Database.exec_request("""Select e.idPlayer, name, profilPicture, score, idGame, nbTournaments, prefix from players p natural join elos e join 
                (SELECT
            idPlayer,
            MAX(date) AS date_max FROM
            elos
        GROUP BY
            idPlayer) sub
			on e.idPlayer = sub.idPlayer
    AND e.date = sub.date_max
        where (nbTournaments >= ? and idGame = ?) order by score desc""", (NUMBER_OF_TOURNAMENTS_TO_BE_RANKED, videogame_id,))
        for row in res:
            player : Player = Player()
            if not row[0] in players.keys():
                data_player = {
                    "id": row[0],
                    "gamerTag": row[1],
                    "user" : {
                        "images": [{ "url" : row[2], "type" : "profile" }]
                    },
                    "nbTournaments": row[5],
                    "prefix": row[6]
                }
                player.hydrate(data_player)
            else:
                player = players[row[0]]
            elo = Elo()
            data_elo = {
                "score": row[3],
                "videogame": {
                    "id": row[4]
                }
            }
            elo.hydrate(data_elo)
            player.Elos[row[4]] = elo
            players[row[0]] = player
        return players
    
    def add_players(self, players : [Player]):
        """
        Ajoute des joueurs en base de données

        Args:
            players ([Player]): Liste des joueurs à ajouter
        """
        req_players = "INSERT INTO players VALUES"
        params_players = []
        for player in players:
            #Gestion de l'ajout dans la table players
            req_players += " (?, ?, ?, ?, ?),"
            params_players.append(player.Id)
            params_players.append(player.Name)
            if "profile" in player.Images.keys():
                params_players.append(player.Images["profile"])
            else:
                params_players.append("")
            params_players.append(player.Prefix)
            params_players.append(player.NbTournaments)

        #Insertion des données des joueurs
        req_players = req_players[:-1]
        super().Database.exec_request(req_players, params_players)

    def remove_all_players(self):
        """
        Supprime tous les joueurs de la base de données
        """
        super().Database.exec_request("DELETE from players")  
    
    #endregion