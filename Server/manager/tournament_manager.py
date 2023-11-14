from model.tournament import Tournament
from model.videogame import Videogame
from data_processing.api.startgg.tournament.ITournamentDao import ITournamentDao as ITournamentDaoAPI
from data_processing.api.startgg.tournament.TournamentDao import TournamentDao as TournamentDaoAPI

class TournamentManager():
    """
    Classe permettant de gérer les tournois
    """

    def __init__(self):
        self.__sg: ITournamentDaoAPI = TournamentDaoAPI()

    # region Operations

    def get_tournaments_by_location(self, date : int, videogame : Videogame, coordonnees : str, distance : str) -> [Tournament]:
        """
        Récupère les tournois par localisation.

        Args:
            date (int): La date.
            videogame (Videogame): Le jeu vidéo.
            coordonnees (str): Les coordonnées.
            distance (str): La distance.

        Returns:
            [Tournament]: Les tournois.

        Raises:
            HTTPError: Si la requête échoue.
        """
        
        return self.__sg.get_tournaments_by_location(date, videogame, coordonnees, distance)

    #endregion