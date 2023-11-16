from data_processing.sql.season.ISeasonDaoSql import ISeasonDaoSql
from data_processing.sql.season.SeasonDaoSql import SeasonDaoSql
from model.season import Season

class SeasonManager():
    """
    Classe permettant de gérer les saisons
    """

    def __init__(self) -> None:
        self.__db: ISeasonDaoSql = SeasonDaoSql()

    # region Operations

    def get_season_by_id(self, id : int) -> Season:
        """
        Renvoie une saison par son id.

        Args:
            id (int): L'id de la saison.

        Returns:
            Season: La saison.

        Raises:
            HTTPError: Si la requête échoue ou qu'il n'y a pas de saison avec cet id.
        """
        return self.__db.get_season_by_id(id)
    
    def get_all_seasons(self) -> [Season]:
        """
        Retourne toutes les saisons

        Args:
            None

        Returns:
            [Season]: Liste des saisons

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__db.get_all_seasons()
    
    def update_season(self, id_season : int, number : int, start_date : int, end_date : int):
        """
        Met à jour une saison dans la base de données

        Args:
            id_season (int): Id de la saison
            number (int): Numéro de la saison
            start_date (int): Date de début de la saison en temps unix
            end_date (int): Date de fin de la saison en temps unix

        Raises:
            HTTPError: Si la requête échoue.
        """
        season = Season()
        season.Id = id_season
        season.Number = number
        season.StartDate = start_date
        season.EndDate = end_date
        self.__db.update_season(season)

    def remove_season(self, idSeason : int):
        """
        Supprime une saison de la base de données

        Args:
            idSeason (int): Id de la saison à supprimer

        Raises:
            HTTPError: Si la requête échoue.
        """
        self.__db.remove_season(idSeason)

    def add_season(self, number : int, start_date : int, end_date : int):
        """
        Ajoute une saison à la base de données

        Args:
            number (int): Numéro de la saison
            start_date (int): Date de début de la saison en temps unix
            end_date (int): Date de fin de la saison en temps unix

        Raises:
            HTTPError: Si la requête échoue.
        """
        season = Season()
        season.Number = number
        season.StartDate = start_date
        season.EndDate = end_date
        self.__db.add_season(season)

    #endregion


