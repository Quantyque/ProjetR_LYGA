from model.elo import Elo
from data_processing.sql.elo.IEloDaoSql import IEloDaoSql
from data_processing.sql.elo.EloDaoSql import EloDaoSql


class EloManager():
    """
    Classe permettant de gérer les elos
    """

    def __init__(self):
        self.__db: IEloDaoSql = EloDaoSql()

    def get_default_elo(self, id_player : int, id_videogame : int) -> int:
        """
        Récupère l'elo par défaut d'un joueur pour un jeu vidéo.

        Args:
            id_player (int): L'id du joueur.
            id_videogame (int): L'id du jeu vidéo.

        Returns:
            int: L'elo par défaut.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.get_default_elo(id_player, id_videogame)
    
    def add_default_elo(self, id_player : int, id_videogame : int) -> None:
        """
        Ajoute un elo par défaut à un joueur pour un jeu vidéo.

        Args:
            id_player (int): L'id du joueur.
            id_videogame (int): L'id du jeu vidéo.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.add_default_elo(id_player, id_videogame)

    def edit_elo(self, id_player : int, id_videogame : int, elo : int) -> None:
        """
        Edition de l'elo d'un joueur pour un jeu vidéo.

        Args:
            id_player (int): L'id du joueur.
            id_videogame (int): L'id du jeu vidéo.
            elo (int): Le nouvel elo.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.edit_elo(id_player, id_videogame, elo)

    def delete_default_elo(self, id_player : int, id_videogame : int) -> None:
        """
        Supprime l'elo par défaut d'un joueur pour un jeu vidéo.

        Args:
            id_player (int): L'id du joueur.
            id_videogame (int): L'id du jeu vidéo.
        
        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.delete_default_elo(id_player, id_videogame)

    def add_elos(self, players : dict, videogame_id : int, date : int) -> None:
        """
        Ajoute des elos à la base de données.

        Args:
            players (dict): Dictionnaire contenant les id des joueurs et leurs elos.
            videogame_id (int): L'id du jeu vidéo.
            date (int): La date de l'ajout.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.add_elos(players, videogame_id, date)

    def delete_all_elos_from_videogame(self, videogame_id : int) -> None:
        """
        Supprime tous les elos d'un jeu vidéo.

        Args:
            videogame_id (int): L'id du jeu vidéo.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.delete_all_elos_from_videogame(videogame_id)

    def get_history_elos(self, player_id : int) -> [Elo]:
        """
        Récupère l'historique des elos d'un joueur.	

        Args:
            player_id (int): L'id du joueur.

        Returns:
            list: Liste des elos.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.get_history_elos(player_id)