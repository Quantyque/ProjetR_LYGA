from model.player import Player
from data_processing.api.startgg.player.IPlayerDaoApi import IPlayerDaoApi
from data_processing.api.startgg.player.PlayerDaoApi import PlayerDaoApi
from data_processing.sql.player.IPlayerDaoSql import IPlayerDaoSql
from data_processing.sql.player.PlayerDaoSql import PlayerDaoSql

class PlayerManager():
    """
    Classe permettant de gérer les joueurs
    """

    def __init__(self):
        self.__sg: IPlayerDaoApi = PlayerDaoApi()
        self.__db: IPlayerDaoSql = PlayerDaoSql()

    # region Operations

    def get_player_by_id(self, id : int) -> Player:
        """
        Récupère un joueur par son id.

        Args:
            id (int): L'id du joueur.

        Returns:
            Player: Le joueur.

        Raises:
            HTTPError: Si la requête échoue.
        """
        player : Player = self.__sg.get_player_by_id(id)
        return self.__db.get_player_by_id(player.Id)
    
    def get_all_players(self) -> [Player]:
        """
        Récupère tous les joueurs.

        Returns:
            [Player]: Les joueurs.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.get_all_players()
    
    def get_ranked_players(self, videogame_id : int) -> [Player]:
        """
        Récupère tous les joueurs classés dans un jeu vidéo.

        Args:
            videogame_id (int): L'id du jeu vidéo.

        Returns:
            [Player]: Les joueurs.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.get_ranked_players(videogame_id)
    
    def add_players(self, players : [Player]):
        """
        Ajouter des joueurs à la base de données.

        Args:
            players ([Player]): Les joueurs.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.add_players(players)

    def remove_all_players(self):
        """
        Supprime tous les joueurs de la base de données.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.remove_all_players()
    
    #endregion