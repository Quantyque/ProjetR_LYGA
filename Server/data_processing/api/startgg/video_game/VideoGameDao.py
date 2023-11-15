from data_processing.api.startgg.video_game.IVideoGameDao import IVideoGameDao
from model.videogame import Videogame
from data_processing.api.startgg.StartGGDao import StartGGDao
from data_processing.api.IApiDao import IApiDao
from exceptions import BadRequestException

class VideoGameDao(IVideoGameDao):

    def __init__(self) -> None:
        self.__api: IApiDao = StartGGDao()

    def get_all_video_games(self):
        """
        Récupère tous les jeux vidéo.

        Returns:
            list[Videogame]: La liste des jeux vidéo.

        Raises:
            Exception: Si la requête échoue.
        """

        video_game: Videogame = Videogame()
        response = self.__api.request_api("""
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

        if response["errors"]:
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

        if response["errors"]:
            raise BadRequestException(response["errors"][0]["message"])
        
        response = self.__api.request_api(graphql_query, params)
        videogame = Videogame()
        videogame.hydrate(response["data"]["videogame"])
        return videogame