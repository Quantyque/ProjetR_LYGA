from model.videogame import Videogame
from abc import ABC, abstractmethod

class IVideoGameDao(ABC):

    @abstractmethod
    def get_all_video_games(self):
        """
        Récupère tous les jeux vidéo.

        Returns:
            list[Videogame]: La liste des jeux vidéo.

        Raises:
            Exception: Si la requête échoue.
        """
        pass