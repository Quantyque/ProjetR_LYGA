from data_processing.api.startgg.video_game.IVideoGameDaoApi import IVideoGameDaoApi
from model.videogame import Videogame
from data_processing.api.api import Api
from exceptions import BadRequestException

class VideoGameDaoApi(IVideoGameDaoApi, Api):

    def __init__(self) -> None:
        super().__init__()

    def get_all_video_games(self):
        """
        Récupère tous les jeux vidéo.

        Returns:
            list[Videogame]: La liste des jeux vidéo.

        Raises:
            Exception: Si la requête échoue.
        """

        video_game: Videogame = Videogame()
        response = self.sg.request_api("""
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

        if "errors" in response and response["errors"]:
            raise BadRequestException(response["errors"][0]["message"])

        video_games = []

        if "data" in response and "videogames" in response["data"]:
            for node in response["data"]["videogames"]["nodes"]:
                video_game = Videogame()
                video_game.hydrate(node)
                video_games.append(video_game)

        return video_games 
    
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
        
        response = self.sg.request_api(graphql_query, params)

        if "errors" in response:
            raise BadRequestException(response["errors"][0]["message"])
    
        videogame = Videogame()
        videogame.hydrate(response["data"]["videogame"])
        return videogame