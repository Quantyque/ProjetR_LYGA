from data_processing.api.startgg.video_game.IVideoGameDao import IVideoGameDao
from model.videogame import Videogame
from data_processing.api.startgg.StartGGDao import StartGGDao
from data_processing.api.IApiDao import IApiDao

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

        video_games = []

        if "data" in response and "videogames" in response["data"]:
            for node in response["data"]["videogames"]["nodes"]:
                video_game = Videogame()
                video_game.hydrate(node)
                video_games.append(video_game)

        return video_games 