from model.tournament import Tournament
from model.videogame import Videogame
from abc import ABC, abstractmethod

class ITournamentDaoApi(ABC):

    @abstractmethod
    def get_tournaments_by_location(self, date : int, videogame : Videogame, coordonnees : str, distance : str) -> [Tournament]:
        """
        Récupère les tournois à une date et un jeu vidéo donnés.

        Args:
            date (int): La date.
            videogame (Videogame): Le jeu vidéo.

        Returns:
            [Tournament]: La liste des tournois.

        Raises:
            Exception: Si la requête échoue.
        """
        pass