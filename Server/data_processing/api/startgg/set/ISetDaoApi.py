from model.set import Set
from abc import ABC, abstractmethod

class ISetDaoApi(ABC):

    @abstractmethod
    def get_last_sets_by_player(self, idPlayer : int, page : int) -> [Set]:
        """
        Retourne les 10 sets d'un joueur en fonction d'une page.

        Args:
            idPlayer (int): L'id du joueur.
            page (int): La page à afficher.

        Returns:
            [Set]: Les sets.

        Raises:
            Exception: Si la requête échoue.
        """
        pass