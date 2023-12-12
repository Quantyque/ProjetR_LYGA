from model.tournament import Tournament
from model.videogame import Videogame
from abc import ABC, abstractmethod

class ITournamentDaoApi(ABC):

    @abstractmethod
    def get_tournaments_by_location(self, afterDate : int, beforeDate : int, videogame : Videogame, coordonnees : str, distance : str) -> [Tournament]:
        """
        Récupère les tournois à une date et un jeu vidéo donnés.

        Args:
            afterDate (int): La date a partir de laquelle rechercher les tournois.
            beforeDate (int): La date jusqu'à laquelle rechercher les tournois.
            videogame (Videogame): Le jeu vidéo.
            coordonnees (str): coordonnees de la localisation des tournois à récupérer
            distance (str): distance de la localisation des tournois à récupérer

        Returns:
            [Tournament]: La liste des tournois.

        Raises:
            Exception: Si la requête échoue.
        """
        pass