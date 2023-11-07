from flask import jsonify
from exceptions import DuplicateGame, GameNotAudited
from model.videogame import Videogame
from manager.manager import Manager


class VideoGameManager(Manager):

    def __init__(self):
        super().__init__()

    # region Operations
    def get_all_video_game(self):
        """
        Get all video games from the StartGG API.

        Returns:
            list: List of video games.

        Raises:
            HTTPError: If the request fails.
        """
        video_game: Videogame = Videogame()
        response = self.request_api("""
        {
            videogames(query: {}) {
                nodes {
                    id
                    name
                    characters {
                        id
                        name
                        images{
                            url
                        }
                    }
                    images {
                        url
                    }
                }
            }
        }
        """)

        video_games = []

        if "data" in response and "videogames" in response["data"]:
            for node in response["data"]["videogames"]["nodes"]:
                video_game = Videogame()
                video_game.hydrate(node)
                video_games.append(video_game)

        return video_games

    def add_audited_game(self, game: Videogame):
        """
        Add a video game to the audited games.

        Args:
            game (VideoGame): The video game to add.

        Raises:
            DuplicateGame: If the game already exists.
        """
        
        rows = self.Database.exec_request("SELECT * FROM Games WHERE idGame = ?", (game.Id,))
        if len(rows) == 0:
            image = ""
            if len(game.Images) > 0:
                image = game.Images[0]
            self.Database.exec_request("INSERT INTO Games(idGame, name, imageUrl) VALUES (?, ?, ?)", (game.Id, game.Name, image))
        else:
            raise DuplicateGame(f"Game with id {game.Id} already exists.")
        
        return jsonify({"message": "Game added successfully."})

    def list_audited_game(self):
        """
        List all audited games.

        Returns:
            list: List of audited games.

        Raises:
            GameNotAudited: If there are no audited games.
        """
        rows = self.Database.exec_request("SELECT * FROM Games")

        result = []
        for row in rows:
            video_game = Videogame()
            video_game.Id = row[0]
            video_game.Name = row[1]
            result.append(video_game)

        return jsonify([{"id": game.Id, "name": game.Name} for game in result])
    
    def update_audited_game(self, game: Videogame):
        """
        Update a video game from the audited games.
        
        Args:
            game (VideoGame): The video game to update.

        Raises:
            GameNotAudited: If the game does not exist.
        """

        game_to_update = self.Database.exec_request("SELECT * FROM Games WHERE idGame = ?", (game.Id,))

        if len(game_to_update) != 0:
            self.Database.exec_request("UPDATE Games SET name = ? WHERE idGame = ?", (game.Name, game.Id))
        else:
            raise GameNotAudited(f"Game with id {game.Id} not audited.")
        
        return jsonify({"message": "Game updated successfully."})

    def delete_audited_game(self, game: Videogame):
        """
        Delete a video game from the audited games.
        
        Args:
            game (VideoGame): The video game to delete.

        Raises:
            GameNotAudited: If the game does not exist.
        """
        rows = self.Database.exec_request("SELECT * FROM Games WHERE idGame = ?", (game.Id,))
        if len(rows) != 0:
            self.Database.exec_request("DELETE FROM Games WHERE idGame = ?", (game.Id,))
        
        return jsonify({"message": "Game deleted successfully."})
    

    def get_video_game_by_id(self, id: int):
        """
        Get a video game by its id.

        Args:
            id (int): The id of the video game.

        Returns:
            VideoGame: The video game.
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
    # endregion