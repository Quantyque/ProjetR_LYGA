from data_processing.sql.player.IPlayerDao import IPlayerDao
from model.player import Player
from model.elo import Elo
from model.videogame import Videogame
from constants import NUMBER_OF_TOURNAMENTS_TO_BE_RANKED
from data_processing.sql.idatabase import IDatabase
from data_processing.sql.sqlite_database import SQLiteDatabase

class PlayerDao(IPlayerDao):

    def __init__(self) -> None:
        self.__db : IDatabase = SQLiteDatabase()

    def get_player_by_id(self, id : int) -> Player:
        """
        Retourne un joueur par son id

        Args:
            id (int): Id du joueur

        Returns:
            Player: Joueur

        Raises:
            HTTPError: Si la requête échoue.
        """

        player : Player = Player()

        # Get player data from database
        res = self.__db.exec_request("""Select idElo, score, p.idPlayer, idGame, name from players p natural join elos e join 
                        (SELECT
                        idPlayer,
                        MAX(date) AS date_max FROM
                        elos
                    GROUP BY
                        idPlayer having (idPlayer = ?)) sub
                        on e.idPlayer = sub.idPlayer
                        AND e.date = sub.date_max""", (id,))

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
        Retourne tous les joueurs

        Returns:
            [Player]: Liste des joueurs
        
        Raises:
            HTTPError: Si la requête échoue.
        """
        players = {}
        res = self.__db.exec_request("""Select p.idPlayer, name, profilPicture, score, idGame, nbTournaments, prefix from players p natural join elos e join 
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
        Retourne tous les joueurs classés dans un jeu vidéo

        Args:
            videogame_id (int): Id du jeu vidéo

        Returns:
            [Player]: Liste des joueurs

        Raises:
            HTTPError: Si la requête échoue.
        """
        players = {}
        res = self.__db.exec_request("""Select e.idPlayer, name, profilPicture, score, idGame, nbTournaments, prefix from players p natural join elos e join 
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

    def add_players(self, players : [Player]) -> None:
        """
        Ajoute des joueurs à la base de données

        Args:
            players ([Player]): Liste des joueurs

        Raises:
            HTTPError: Si la requête échoue.
        """
        req_players = "INSERT INTO players VALUES"
        params_players = []
        for player in players:
            # Manage the addition in the players table
            req_players += " (?, ?, ?, ?, ?),"
            params_players.append(player.Id)
            params_players.append(player.Name)
            if "profile" in player.Images.keys():
                params_players.append(player.Images["profile"])
            else:
                params_players.append("")
            params_players.append(player.Prefix)
            params_players.append(player.NbTournaments)

        # Insert players
        req_players = req_players[:-1]
        self.__db.exec_request(req_players, params_players)

    def remove_all_players(self) -> None:
        """
        Supprime tous les joueurs de la base de données

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        self.__db.exec_request("DELETE from players") 