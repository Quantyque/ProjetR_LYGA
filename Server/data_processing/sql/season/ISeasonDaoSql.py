from abc import ABC, abstractmethod
from model.season import Season
from data_processing.sql.dao import Dao

class ISeasonDaoSql(ABC, Dao):
    """
    Interface du DAO des saisons
    """

    @abstractmethod
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
        pass

    @abstractmethod
    def add_season(self, season : Season) -> None:
        """
        Ajoute une saison à la base de données

        Args:
            season (Season): Saison à ajouter

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def remove_season(self, idSeason : int) -> None:
        """
        Supprime une saison de la base de données

        Args:
            idSeason (int): Id de la saison à supprimer

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def update_season(self, season : Season) -> None:
        """
        Met à jour une saison dans la base de données

        Args:
            season (Season): Saison à mettre à jour

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def get_season_by_id(self, id : int) -> Season:
        """
        Retourne une saison par son id.

        Args:
            id (int): L'id de la saison.

        Returns:
            Season: La saison.

        Raises:
            HTTPError: Si la requête échoue ou qu'il n'y a pas de saison avec cet id.
        """
        pass