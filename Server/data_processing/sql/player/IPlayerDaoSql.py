from abc import ABC, abstractmethod
from model.player import Player

class IPlayerDaoSql(ABC):

    @abstractmethod
    def get_all_players(self) -> [Player]:
        """
        Retourne tous les joueurs

        Returns:
            [Player]: Liste des joueurs
        
        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def add_players(self, players : [Player]):
        """
        Ajoute des joueurs à la base de données

        Args:
            players ([Player]): Liste des joueurs

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def remove_all_players(self):
        """
        Supprime tous les joueurs de la base de données

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass