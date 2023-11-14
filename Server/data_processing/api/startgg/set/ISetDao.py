from model.set import Set
from abc import ABC, abstractmethod

class ISetDao(ABC):

    @abstractmethod
    def get_last_sets_by_player(self, idPlayer : int) -> [Set]:
        """
        Retournes les 3 derniers sets d'un joueur.

        Args:
            idPlayer (int): L'id du joueur.

        Returns:
            [Set]: Les sets.

        Raises:
            Exception: Si la requête échoue.
        """
        pass