from data_processing.api.startgg.set.ISetDao import ISetDao
from model.set import Set
from data_processing.api.startgg.StartGGDao import StartGGDao
from data_processing.api.IApiDao import IApiDao
from exceptions import BadRequestException

class SetDao(ISetDao):

    def __init__(self) -> None:
        self.__api: IApiDao = StartGGDao()

    # region : Operations
    def get_last_sets_by_player(self, idPlayer : int) -> [Set]:
        """
        Retournes les 3 derniers sets d'un joueur.

        Args:
            idPlayer (int): L'id du joueur.

        Returns:
            [Set]: Les sets.

        Raises:
            Exception: Si la requête échoue.
        """

        response = self.__api.request_api("""
                            query SetsByPlayer($idPlayer : ID!) {
                                                player(id: $idPlayer) {
                                                    sets(perPage: 3) {
                                                    nodes {
                                                        id
                                                        round
                                                        winnerId
                                                        completedAt
                                                        event{
                                                            videogame{
                                                                id
                                                                name
                                                            }
                                                        }
                                                        games{
                                                            id
                                                            winnerId
                                                            selections{
                                                                entrant{
                                                                    id
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
                                                        slots{
                                                            entrant{
                                                                id
                                                                name
                                                                isDisqualified
                                                                standing{
                                                                    player{
                                                                        id
                                                                        prefix
                                                                        gamerTag
                                                                        user{
                                                                            images{
                                                                                url
                                                                                type
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                    """, {
                        "idPlayer": idPlayer
                    })
        
        if response["errors"]:
            raise BadRequestException(response["errors"][0]["message"])
        
        sets = []
        if "data" in response:
            for data_set in response['data']['player']['sets']['nodes']:
                set = Set()
                set.hydrate(data_set)
                sets.append(set)
        return sets
    
    # endregion