from model.player import Player
from abc import ABC, abstractmethod


class IPlayerDao(ABC):

    @abstractmethod
    def get_player_by_id(self, id : int) -> Player:
        """
        Récupère un joueur par son id.

        Args:
            id (int): L'id du joueur.

        Returns:
            Player: Le joueur.

        Raises:
            Exception: Si la requête échoue.
        """
        pass