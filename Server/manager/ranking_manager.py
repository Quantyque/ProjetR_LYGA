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

    def update_ranking(self, date : int, videogame_id : int, coordonnees : str, distance : str) -> Dict[int, str]:
        """
        Mise à jour du classement d'un jeu vidéo.

        Args:
            date (int): La date.
            videogame_id (int): L'id du jeu vidéo.
            coordonnees (str): Les coordonnées.
            distance (str): La distance.

        Returns:
            Dict[int, str]: Le classement.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.update_ranking(date, videogame_id, coordonnees, distance)

    #endregion