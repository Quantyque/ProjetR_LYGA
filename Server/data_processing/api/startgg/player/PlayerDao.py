from data_processing.api.startgg.player.IPlayerDao import IPlayerDao as IPlayerDaoAPI
from data_processing.api.startgg.StartGGDao import StartGGDao
from data_processing.api.IApiDao import IApiDao
from model.player import Player

class PlayerDao(IPlayerDaoAPI):

    def __init__(self) -> None:
        self.__api: IApiDao = StartGGDao()

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
        player : Player = Player()
        response = self.__api.request_api("""
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
        player.hydrate(response["data"]["player"])

        return player