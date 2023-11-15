from model.videogame import Videogame
from data_processing.api.startgg.video_game.IVideoGameDao import IVideoGameDao as IVideoGameDaoAPI
from data_processing.api.startgg.video_game.VideoGameDao import VideoGameDao as VideoGameDaoAPI
from data_processing.sql.video_game.IVideoGameDao import IVideoGameDao as IVideoGameDaoSQL
from data_processing.sql.video_game.VideoGame import VideoGameDao as VideoGameDaoSQL  


class VideoGameManager():
    """
    Classe permettant de gérer les jeux vidéos
    """

    def __init__(self):
        self.__sg: IVideoGameDaoAPI = VideoGameDaoAPI()
        self.__db: IVideoGameDaoSQL = VideoGameDaoSQL()

    # region Operations
    def get_all_video_game(self):
        """
        Réupère tous les jeux vidéos.

        Returns:
            list: List of video games.

        Raises:
            HTTPError: If the request fails.
        """
        return self.__sg.get_all_video_games()
    
    def get_video_game_by_id(self, id: int):
        """
        Récupère un jeu vidéo par son id.

        Args:
            id (int): L'id du jeu vidéo.

        Returns:
            VideoGame: Le jeu vidéo.

        Raises:
            HTTPError: Si la requête échoue.
        """     
        return self.__sg.get_video_game_by_id(id)

    def add_audited_game(self, game: Videogame):
        """
        Ajoute un jeu vidéo à la liste des jeux audités.

        Args:
            game (VideoGame): Le jeu vidéo à ajouter.

        Raises:
            GameAlreadyAudited: Si le jeu vidéo existe déjà.
        """
        return self.__db.add_audited_game(game)
        
    def list_audited_game(self):
        """
        Liste les jeux vidéos audités.

        Returns:
            list: liste des jeux vidéos audités.

        Raises:
            GameNotAudited: Si le jeu vidéo n'existe pas.
        """
        return self.__db.list_audited_game()

    def update_audited_game(self, game: Videogame):
        """
        Met à jour un jeu vidéo de la liste des jeux audités.

        Args:
            game (VideoGame): Le jeu vidéo à mettre à jour.

        Raises:
            GameNotAudited: Si le jeu vidéo n'existe pas.
        """
        return self.__db.update_audited_game(game)

    def delete_audited_game(self, game: Videogame):
        """
        Supprime un jeu vidéo de la liste des jeux audités.

        Args:
            game (VideoGame): Le jeu vidéo à supprimer.

        Raises:
            GameNotAudited: Si le jeu vidéo n'existe pas.
        """
        return self.__db.delete_audited_game(game)
    
    # endregion