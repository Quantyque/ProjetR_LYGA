from model.elo import Elo
from abc import ABC, abstractmethod

class IEloDaoSql(ABC):

    @abstractmethod
    def get_default_elo(self, id_player : int, id_videogame : int) -> int:
        """
        Retourne l'elo par défaut d'un joueur

        Args:
            id_player (int): Id du joueur
            id_videogame (int): Id du jeu vidéo

        Returns:
            int: Elo par défaut du joueur
        """
        pass

    @abstractmethod
    def add_default_elo(self, id_player : int, id_videogame : int) -> None:
        """
        Ajoute un elo par défaut à un joueur

        Args:
            id_player (int): Id du joueur
            id_videogame (int): Id du jeu vidéo

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def edit_elo(self, id_player : int, id_videogame : int, elo : int) -> None:
        """
        Met à jour l'elo d'un joueur

        Args:
            id_player (int): Id du joueur
            id_videogame (int): Id du jeu vidéo
            elo (int): Nouvel elo

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def delete_default_elo(self, id_player : int, id_videogame : int) -> None:
        """
        Supprime l'elo par défaut d'un joueur

        Args:
            id_player (int): Id du joueur
            id_videogame (int): Id du jeu vidéo

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def add_elos(self, players : dict, videogame_id : int, date : int):
        """
        Ajoute les elos d'une partie à la base de données

        Args:
            players (dict): Dictionnaire des joueurs
            videogame_id (int): Id du jeu vidéo
            date (int): Date de la partie

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def delete_all_elos_from_videogame(self, videogame_id : int):
        """
        Supprime tous les elos d'un jeu vidéo

        Args:
            videogame_id (int): Id du jeu vidéo

        Returns:
            None

        Raises:
            HTTPError: Si la requête échoue.
        """
        pass

    @abstractmethod
    def get_history_elos(self, player_id : int) -> [Elo]:
        """
        Retournes l'historique des elos d'un joueur

        Args:
            player_id (int): Id du joueur

        Returns:
            [Elo]: Liste des elos
    
        Raises:
            HTTPError: Si la requête échoue.
        """
        pass
