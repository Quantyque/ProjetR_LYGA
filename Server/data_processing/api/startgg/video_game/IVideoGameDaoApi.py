from model.videogame import Videogame
from abc import ABC, abstractmethod

class IVideoGameDaoApi(ABC):

    @abstractmethod
    def get_all_video_games(self) -> [Videogame]:
        """
        Récupère tous les jeux vidéo.

        Returns:
            list[Videogame]: La liste des jeux vidéo.

        Raises:
            Exception: Si la requête échoue.
        """
        pass

    @abstractmethod
    def get_video_game_by_id(self, id: int) -> Videogame:
        """
        Récupère un jeu vidéo par son id.

        Args:
            id (int): L'id du jeu vidéo.
    
        Returns:
            VideoGame: Le jeu vidéo.

        Raises:
            GameNotAudited: Si le jeu vidéo n'est pas dans la liste.
        """
        pass