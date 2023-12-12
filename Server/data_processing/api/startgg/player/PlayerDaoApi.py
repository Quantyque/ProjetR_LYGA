from data_processing.api.startgg.player.IPlayerDaoApi import IPlayerDaoApi
from model.player import Player
from exceptions import BadRequestException
from data_processing.api.api import Api

class PlayerDaoApi(IPlayerDaoApi, Api):

    def __init__(self) -> None:
        super().__init__()

    def get_player_by_id(self, id : int) -> Player:
        """
        Récupère un joueur par son id.

        Args:
            id (int): L'id du joueur.

        Returns:
            Player: Le joueur.

        Raises:
            Exception: Si la requête échoue.
        """
        # Récupération du joueur
        player : Player = Player()
        response = self.sg.request_api("""
                query PlayerById($idPlayer : ID!) {
                    player(id: $idPlayer) {
                        id
                        prefix
                        gamerTag
                        user{
                            authorizations{
                            url
                            }  
                            images{
                            url
                            type
                            }
                            bio
                        }
                        sets(perPage: 25) {
                        nodes {
                            id
                            event{
                            videogame{
                                id,
                                name
                            }
                            }
                            games{
                                selections{
                                    entrant{
                                        standing{
                                            player{
                                                id
                                                gamerTag
                                            }
                                        }
                                    }
                                    character{
                                        id
                                        name
                                       images{
                                        url
                                       }
                                    }
                                }
                            }
                        }
                        }
                    }
                    }
                    """,
                    {"idPlayer" : id})
        
        # Gestion des erreurs
        if "errors" in response:
            raise BadRequestException(response["errors"][0]["message"])
        
        # Hydratation du joueur en fonction des données récupérées
        player.hydrate(response["data"]["player"])

        return player