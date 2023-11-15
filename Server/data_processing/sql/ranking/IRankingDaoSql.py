from model.ranking import Ranking
from abc import ABC, abstractmethod
from typing import Dict

class IRankingDaoSql(ABC):

    @abstractmethod
    def update_ranking(self, date : int, videogame_id : int, coordonnees : str, distance : str) -> Dict[int, str]:
        """
        Met à jour le classement

        Args:
            date (int): date
            videogame_id (int): videogame's id
            coordonnees (str): coordinates
            distance (str): distance

        Returns:
            dict[int, str]: in key the player's id and in value the player himself

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass