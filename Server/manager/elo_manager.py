from manager.manager import Manager
from model.elo import Elo
from model.videogame import Videogame


class EloManager(Manager):
    """
    Classe permettant de gérer les elos
    """
    def __init__(self):
        super().__init__()

    def get_default_elo(self, id_player : int, id_videogame : int) -> int:
        """
        Renvoie la valeur par défaut de l'élo d'un joueur
        """
        res = [[]]
        res = super().Database.exec_request("SELECT defaultElo FROM defaultPlayerElos WHERE idPlayer = ? and idGame = ?", (id_player,id_videogame))
        if len(res) == 0:
            res.append([])
            res[0].append(1000)
            super().Database.exec_request("INSERT INTO defaultPlayerElos VALUES (null, ?, ?, ?)", (1000, id_player, id_videogame))
        return res[0][0]
    
    def add_default_elo(self, id_player : int, id_videogame : int) -> None:
        """
        Ajout une valeur d'élo par défaut à un joueur
        """
        super().Database.exec_request("INSERT INTO defaultPlayerElos VALUES (null, ?, ?, ?)", (1000, id_player, id_videogame))

    def edit_elo(self, id_player : int, id_videogame : int, elo : int) -> None:
        """
        Modifie l'élo d'un joueur
        """
        super().Database.exec_request("UPDATE defaultPlayerElos SET score = ? WHERE idPlayer = ? and idGame = ?", (elo, id_player, id_videogame))

    def delete_default_elo(self, id_player : int, id_videogame : int) -> None:
        """
        Supprime l'élo par défaut d'un joueur
        """
        super().Database.exec_request("DELETE FROM defaultPlayerElos WHERE idPlayer = ? and idGame = ?", (id_player, id_videogame))

    def add_elos(self, players : dict, videogame_id : int, date : int):
        """
        Ajoute des elos en base de données

        Args:
            players (dict): Dictionnaire des joueurs à ajouter avec en clé leur id
            videogame_id (int): Id du jeu auquel l'elo correspond
            date (int): Date à laquelle l'elo a été calculé
        """
        #Ajout des elos dans la base de données si l'elo n'existe pas ou si l'elo a changé
        players_to_add = []
        for player_id in players:
            res = super().Database.exec_request("SELECT idPlayer, idGame, score, date FROM elos WHERE idGame = ? and idPlayer = ? order by date limit 1", [videogame_id, player_id])
            if len(res) == 0 or res[0][2] != players[player_id].Elos[videogame_id].Score:
                players_to_add.append(player_id)
        #Création de la requête d'ajout des elos
        req_elos = "INSERT INTO elos VALUES"
        params_elos = []
        for player_id in players_to_add:
            #Gestion de l'ajout dans la table Elos
            req_elos += " (null,?, ?, ?, ?),"
            params_elos.append(players[player_id].Elos[videogame_id].Score)
            params_elos.append(player_id)
            params_elos.append(videogame_id)
            params_elos.append(date)
                
        #Insertion des données des elos
        if len(players_to_add) > 0:
            req_elos = req_elos[:-1]
            super().Database.exec_request(req_elos, params_elos)

    def delete_all_elos_from_videogame(self, videogame_id : int):
        """
        Supprime tous les elos de la base de données

        Args:
            videogame_id (int): Id du jeu auquel les elos correspondent
        """
        super().Database.exec_request("DELETE from elos where idGame = ?", [videogame_id])

    def get_history_elos(self, player_id : int) -> [Elo]:
        """
        Renvoie l'hitorique d'elo du joueur
        """
        res = super().Database.exec_request("SELECT score, date, idGame, name FROM elos natural join games WHERE idPlayer = ? ORDER BY date", (player_id,))
        elos = []
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