from data_processing.sql.player.IPlayerDaoSql import IPlayerDaoSql
from model.player import Player
from model.elo import Elo
from constants import NUMBER_OF_TOURNAMENTS_TO_BE_RANKED
from data_processing.sql.dao import Dao

class PlayerDaoSql(IPlayerDaoSql, Dao):

    def __init__(self) -> None:
        super().__init__()
    
    def get_all_players(self) -> [Player]:
        """
        Retourne tous les joueurs

        Returns:
            [Player]: Liste des joueurs
        
        Raises:
            HTTPError: Si la requête échoue.
        """
        players = {}
        res = self.db.exec_request("""Select p.idPlayer, name, profilPicture, score, idGame, nbTournaments, prefix, idSeason from players p natural join elos e join 
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
                },
                "season": {
                    "id": row[7]
                }
            }
            elo.hydrate(data_elo)
            player.Elos[row[4]] = elo
            players[row[0]] = player
        return players

    def get_ranked_players(self, videogame_id : int, season_id : int) -> [Player]:
        """
        Retourne tous les joueurs classés dans un jeu vidéo

        Args:
            videogame_id (int): Id du jeu vidéo
            season_id (int): Id de la saison

        Returns:
            [Player]: Liste des joueurs

        Raises:
            HTTPError: Si la requête échoue.
        """
        players = {}
        res = self.db.exec_request("""Select e.idPlayer, name, profilPicture, score, idGame, nbTournaments, prefix, idSeason from players p natural join elos e join 
                (SELECT
            idPlayer,
            MAX(date) AS date_max FROM
            elos
        GROUP BY
            idPlayer) sub
			on e.idPlayer = sub.idPlayer
    AND e.date = sub.date_max
        where (nbTournaments >= ? and idGame = ? and idSeason = ?) order by score desc""", (NUMBER_OF_TOURNAMENTS_TO_BE_RANKED, videogame_id, season_id))
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
                },
                "season": {
                    "id": row[7]
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
        self.db.exec_request(req_players, params_players)

    def remove_all_players(self) -> None:
        """
        Supprime tous les joueurs de la base de données

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        self.db.exec_request("DELETE from players") 