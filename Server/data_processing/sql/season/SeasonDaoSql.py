from model.season import Season
from data_processing.sql.season.ISeasonDaoSql import ISeasonDaoSql
import datetime as dt
import time

class SeasonDaoSql(ISeasonDaoSql):
    """
    DAO des saisons
    """

    def __init__(self):
        super().__init__()

    def get_current_season(self) -> Season:
        """
        Retourne la saison courante

        Args:
            None

        Returns:
            Season: Saison courante

        Raises:
            HTTPError: Si la requête échoue.
        """
        current_date = dt.datetime.today()
        unix_date = time.mktime(current_date.timetuple())
        res = self.db.exec_request("""SELECT idSeason, number, startDate, endDate FROM seasons WHERE startDate <= ? AND endDate >= ?""", (unix_date, unix_date))
        if len(res) == 0:
            raise Exception("No current season")
        season : Season = Season()
        data_season = {
            "id" : res[0][0],
            "number" : res[0][1],
            "startDate" : res[0][2],
            "endDate" : res[0][3]
        }
        season.hydrate(data_season)
        return season
    
    def add_season(self, season : Season):
        """
        Ajoute une saison à la base de données

        Args:
            season (Season): Saison à ajouter

        Raises:
            HTTPError: Si la requête échoue.
        """
        self.db.exec_request("""INSERT INTO seasons VALUES (null, ?, ?, ?)""", (season.Number, season.StartDate, season.EndDate))

    def remove_season(self, idSeason : int):
        """
        Supprime une saison de la base de données

        Args:
            idSeason (int): Id de la saison à supprimer

        Raises:
            HTTPError: Si la requête échoue.
        """
        self.db.exec_request("""DELETE FROM seasons WHERE idSeason = ?""", (idSeason,))

    def update_season(self, season : Season):
        """
        Met à jour une saison dans la base de données

        Args:
            season (Season): Saison à mettre à jour

        Raises:
            HTTPError: Si la requête échoue.
        """
        self.db.exec_request("""UPDATE seasons SET number = ?, startDate = ?, endDate = ? WHERE idSeason = ?""", (season.name, season.start_date, season.end_date, season.id_season))

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
        res = self.db.exec_request("""SELECT idSeason, number, startDate, endDate FROM seasons""")
        seasons = []
        for row in res:
            season : Season = Season()
            data_season = {
                "id" : row[0],
                "number" : row[1],
                "startDate" : row[2],
                "endDate" : row[3]
            }
            season.hydrate(data_season)
            seasons.append(season)
        return seasons
    
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
        res = self.db.exec_request("""SELECT idSeason, number, startDate, endDate FROM seasons WHERE idSeason = ?""", (id,))
        if len(res) == 0:
            raise Exception("No season with this id")
        season : Season = Season()
        data_season = {
            "id" : res[0][0],
            "number" : res[0][1],
            "startDate" : res[0][2],
            "endDate" : res[0][3]
        }
        season.hydrate(data_season)
        return season