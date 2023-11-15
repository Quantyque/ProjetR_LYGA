from model.videogame import Videogame
from abc import ABC, abstractmethod

class IVideoGameDaoSql(ABC):

    @abstractmethod
    def add_audited_game(self, game: Videogame) -> str():
        """
        Ajoute un jeu vidéo à la liste des jeux vidéo audités.

        Args:
            game (VideoGame): Le jeu vidéo à ajouter.

        Returns:
            str(): Le message de succès.

        Raises:
            GameAlreadyAudited: Si le jeu vidéo est déjà dans la liste.
        """
        pass

    @abstractmethod
    def list_audited_game(self) -> [Videogame]:
        """
        Liste les jeux vidéo audités.

        Returns:
            [VideoGame]: La liste des jeux vidéo audités.

        Raises:
            NoGameAudited: Si aucun jeu vidéo n'est dans la liste.
        """
        pass

    @abstractmethod
    def update_audited_game(self, game: Videogame) -> str():
        """
        Met à jour un jeu vidéo de la liste des jeux vidéo audités.

        Args:
            game (VideoGame): Le jeu vidéo à mettre à jour.

        Returns:
            str(): Le message de succès.

        Raises:
            GameNotAudited: Si le jeu vidéo n'est pas dans la liste.
        """
        pass
    
    @abstractmethod
    def delete_audited_game(self, game: Videogame) -> str():
        """
        Supprime un jeu vidéo de la liste des jeux vidéo audités.

        Args:
            game (VideoGame): Le jeu vidéo à supprimer.

        Returns:
            str(): Le message de succès.

        Raises:
            GameNotAudited: Si le jeu vidéo n'est pas dans la liste.
        """
        pass