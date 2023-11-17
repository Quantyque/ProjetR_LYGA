from data_processing.api.startgg.video_game.IVideoGameDaoApi import IVideoGameDaoApi
from model.videogame import Videogame
from data_processing.api.api import Api
from exceptions import BadRequestException

class VideoGameDaoApi(IVideoGameDaoApi, Api):

    def __init__(self) -> None:
        super().__init__()

    def get_all_video_games(self) -> [Videogame]:
        """
        Récupère tous les jeux vidéo.

        Returns:
            list[Videogame]: La liste des jeux vidéo.

        Raises:
            Exception: Si la requête échoue.
        """
        # Initialisation du jeu vidéo
        video_game: Videogame = Videogame()
        video_games = []
        # Récupération des jeux vidéo
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
        # Gestions des erreurs
        if "errors" in response and response["errors"]:
            raise BadRequestException(response["errors"][0]["message"])

        # Ajout des jeux vidéo à la liste
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
        # Création de la requête
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
        
        # Envoi de la requête
        response = self.sg.request_api(graphql_query, params)

        # Gestion des erreurs
        if "errors" in response:
            raise BadRequestException(response["errors"][0]["message"])
    
        # Récupération du jeu vidéo
        videogame = Videogame()
        videogame.hydrate(response["data"]["videogame"])
        return videogame