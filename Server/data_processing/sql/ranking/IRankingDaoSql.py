from model.ranking import Ranking
from abc import ABC, abstractmethod
from typing import Dict

class IRankingDaoSql(ABC):

    @abstractmethod
    def update_ranking(self, afterDate : int, beforeDate : int, videogame_id : int, coordonnees : str, distance : str) -> Dict[int, str]:
        """
        Met à jour le classement

        Args:
            afterDate (int): Date à partir de laquelle mettre à jour le classement
            beforeDate (int): Date jusqu'à laquelle mettre à jour le classement
            videogame_id (int): id du jeu vidéo
            coordonnees (str): coordonnees
            distance (str): distance

        Returns:
            dict[int, str]: en clé l'id du joueur et en valeur le rang du joueur

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass