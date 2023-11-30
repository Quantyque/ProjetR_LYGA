from model.elo import Elo
from model.videogame import Videogame
from data_processing.sql.elo.IEloDaoSql import IEloDaoSql
from data_processing.sql.dao import Dao
from model.season import Season

class EloDaoSql(IEloDaoSql, Dao):

    def __init__(self):
        super().__init__()

    def get_default_elo(self, id_player : int, id_videogame : int) -> int:
        """
        Retourne l'elo par défaut d'un joueur

        Args:
            id_player (int): Id du joueur
            id_videogame (int): Id du jeu vidéo

        Returns:
            int: Elo par défaut du joueur
        """
        
        res = [[]]
        res = self.db.exec_request("SELECT defaultElo FROM defaultPlayerElos WHERE idPlayer = ? and idGame = ?", (id_player,id_videogame))

        if len(res) == 0:
            res.append([])
            res[0].append(1000)
            self.db.exec_request("INSERT INTO defaultPlayerElos VALUES (null, ?, ?, ?)", (1000, id_player, id_videogame))

        return res[0][0]
    
    def add_default_elo(self, id_player : int, id_videogame : int, score : int) -> None:
        """
        Ajoute un elo par défaut à un joueur

        Args:
            id_player (int): Id du joueur
            id_videogame (int): Id du jeu vidéo
            score (int): Elo par défaut

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        self.db.exec_request("INSERT INTO defaultPlayerElos VALUES (null, ?, ?, ?)", (score, id_player, id_videogame))

    def edit_elo(self, id_player : int, id_videogame : int, elo : int) -> None:
        """
        Met à jour l'elo d'un joueur

        Args:
            id_player (int): Id du joueur
            id_videogame (int): Id du jeu vidéo
            elo (int): Nouvel elo

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """

        self.db.exec_request("UPDATE defaultPlayerElos SET score = ? WHERE idPlayer = ? and idGame = ?", (elo, id_player, id_videogame))

    def delete_default_elo(self, id_player : int, id_videogame : int) -> None:
        """
        Supprime l'elo par défaut d'un joueur

        Args:
            id_player (int): Id du joueur
            id_videogame (int): Id du jeu vidéo

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """

        self.db.exec_request("DELETE FROM defaultPlayerElos WHERE idPlayer = ? and idGame = ?", (id_player, id_videogame))

    def add_elos(self, players : dict, videogame_id : int, date : int) -> None:
        """
        Ajoute les elos d'une partie à la base de données

        Args:
            players (dict): Dictionnaire des joueurs
            videogame_id (int): Id du jeu vidéo
            date (int): Date de la partie

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """

        players_to_add = []

        for player_id in players:
            # Récupère le dernier elo du joueur pour le jeu vidéo
            res = self.db.exec_request("SELECT idPlayer, idGame, score, date FROM elos WHERE idGame = ? and idPlayer = ? order by date limit 1", [videogame_id, player_id])
            # Ajoute les elos des joueurs qui ne sont pas dans la base de données ou dont l'elo a changé
            if len(res) == 0 or res[0][2] != players[player_id].Elos[videogame_id].Score:
                players_to_add.append(player_id)

        # Création de la requête
        req_elos = "INSERT INTO elos VALUES"
        params_elos = []

        for player_id in players_to_add:
            # Ajoute les attributs des elos à la requête
            req_elos += " (null,?, ?, ?, ?, ?),"
            params_elos.append(players[player_id].Elos[videogame_id].Score)
            params_elos.append(player_id)
            params_elos.append(videogame_id)
            params_elos.append(date)
            params_elos.append(players[player_id].Elos[videogame_id].Season.Id)
                
        # Exectution de la requête
        if len(players_to_add) > 0:
            req_elos = req_elos[:-1]
            self.db.exec_request(req_elos, params_elos)

    def delete_all_elos_from_videogame(self, videogame_id : int) -> None:
        """
        Supprime tous les elos d'un jeu vidéo

        Args:
            videogame_id (int): Id du jeu vidéo

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        
        self.db.exec_request("DELETE from elos where idGame = ?", [videogame_id])

    def get_history_elos(self, player_id : int) -> [Elo]:
        """
        Retournes l'historique des elos d'un joueur

        Args:
            player_id (int): Id du joueur

        Returns:
            [Elo]: Liste des elos
    
        Raises:
            HTTPError: Si la requête échoue.
        """
        # Initialisation de la liste des elos
        elos = []
        # Récupération des elos
        res = self.db.exec_request("SELECT score, date, idGame, name FROM elos natural join games WHERE idPlayer = ? ORDER BY date", (player_id,))

        # Ajout des elos à la liste
        for row in res:
            videogame = Videogame()
            videogame.Id = row[2]
            videogame.Name = row[3]
            elo = Elo()
            data_elo = {
                "score": row[0],
                "date": row[1],
                "videogame": videogame.toJSON()
            }
            elo.hydrate(data_elo)
            elos.append(elo)

        return elos
    
    def get_elos_by_player(self, player_id : int) -> [Elo]:
        """
        Retourne les elos d'un joueur

        Args:
            player_id (int): Id du joueur

        Returns:
            [Elo]: Liste des elos

        Raises:
            HTTPError: Si la requête échoue.
        """
        # Initialisation de la liste des elos
        elos = []

        # Récupération des elos
        res = self.db.exec_request("""Select idElo, score, e.idPlayer, e.idGame, name, idSeason from Games g natural join elos e join 
                        (SELECT
                        idPlayer, idGame,
                        MAX(date) AS date_max FROM
                        elos
                    GROUP BY
                        idPlayer having (idPlayer = ?)) sub
                        on e.idPlayer = sub.idPlayer
                        AND e.date = sub.date_max""", (player_id,))
        
        # Ajout des elos à la liste
        for row in res:
            data_video_game = {
                "id": row[3],
                "name": row[4]
            }
            data_season = {
                "id": row[5]
            }
            elo = Elo()
            dataElo = {
                "id": row[0],
                "score": row[1],
                "videogame": data_video_game,
                "season": data_season
            }
            elo.hydrate(dataElo)
            elos.append(elo)

        return elos