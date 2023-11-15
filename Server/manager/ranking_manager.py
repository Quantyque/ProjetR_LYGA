from data_processing.sql.ranking.IRankingDaoSql import IRankingDaoSql
from data_processing.sql.ranking.RankingDaoSql import RankingDaoSql
from typing import Dict

class RankingManager():
    """
    Classe permettant de gérer les classements
    """

    def __init__(self):
        self.__db: IRankingDaoSql = RankingDaoSql()

    # region Operations

    def update_ranking(self, afterDate : int, beforeDate : int, videogame_id : int, coordonnees : str, distance : str) -> Dict[int, str]:
        """
        Mise à jour du classement d'un jeu vidéo.

        Args:
            afterDate (int): La date a partir de laquelle rechercher les tournois.
            beforeDate (int): La date jusqu'à laquelle rechercher les tournois.
            videogame_id (int): L'id du jeu vidéo.
            coordonnees (str): Les coordonnées.
            distance (str): La distance.

        Returns:
            Dict[int, str]: Le classement.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.update_ranking(afterDate, beforeDate, videogame_id, coordonnees, distance)

    #endregion