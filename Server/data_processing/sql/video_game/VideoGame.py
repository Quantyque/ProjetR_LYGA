from data_processing.sql.video_game.IVideoGameDao import IVideoGameDao
from data_processing.sql.idatabase import IDatabase
from data_processing.sql.sqlite_database import SQLiteDatabase
from flask import jsonify
from exceptions import DuplicateGame, GameNotAudited
from model.videogame import Videogame

class VideoGameDao(IVideoGameDao):

    def __init__(self):
        self.__db : IDatabase = SQLiteDatabase()

    #region Operation

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

        rows = self.__db.exec_request("SELECT * FROM Games WHERE idGame = ?", (game.Id,))
        if len(rows) == 0:
            image = ""
            if len(game.Images) > 0:
                image = game.Images[0]
            self.__db.exec_request("INSERT INTO Games(idGame, name, imageUrl) VALUES (?, ?, ?)", (game.Id, game.Name, image))
        else:
            raise DuplicateGame(f"Game with id {game.Id} already exists.")
        
        return jsonify({"message": "Game added successfully."})

    def list_audited_game(self) -> [Videogame]:
        """
        Liste les jeux vidéo audités.

        Returns:
            [VideoGame]: La liste des jeux vidéo audités.

        Raises:
            NoGameAudited: Si aucun jeu vidéo n'est dans la liste.
        """

        rows = self.__db.exec_request("SELECT * FROM Games")

        result = []
        for row in rows:
            video_game = Videogame()
            video_game.Id = row[0]
            video_game.Name = row[1]
            result.append(video_game)

        return jsonify([{"id": game.Id, "name": game.Name} for game in result])

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
        game_to_update = self.__db.exec_request("SELECT * FROM Games WHERE idGame = ?", (game.Id,))

        if len(game_to_update) != 0:
            self.__db.exec_request("UPDATE Games SET name = ? WHERE idGame = ?", (game.Name, game.Id))
        else:
            raise GameNotAudited(f"Game with id {game.Id} not audited.")
        
        return jsonify({"message": "Game updated successfully."})
    
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

        rows = self.__db.exec_request("SELECT * FROM Games WHERE idGame = ?", (game.Id,))
        if len(rows) != 0:
            self.__db.exec_request("DELETE FROM Games WHERE idGame = ?", (game.Id,))
        
        return jsonify({"message": "Game deleted successfully."})
    
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
        
        graphql_query = """
            query Videogames($id: ID!) {
                videogame(id : $id){
                    id,
                    name,
                    images{
                    url
                    }
                }
                }
        """

        params = {
            "id": id
        }
        
        response = super().request_api(graphql_query, params)
        videogame = Videogame()
        videogame.hydrate(response["data"]["videogame"])
        return videogame

    #endregion