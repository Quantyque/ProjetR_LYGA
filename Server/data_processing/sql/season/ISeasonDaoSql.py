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
    def add_season(self, season : Season):
        """
        Ajoute une saison à la base de données

        Args:
            season (Season): Saison à ajouter

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def remove_season(self, season : Season):
        """
        Supprime une saison de la base de données

        Args:
            season (Season): Saison à supprimer

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def update_season(self, season : Season):
        """
        Met à jour une saison dans la base de données

        Args:
            season (Season): Saison à mettre à jour

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