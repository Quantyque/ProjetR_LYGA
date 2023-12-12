from data_processing.api.startgg.set.ISetDaoApi import ISetDaoApi
from model.set import Set
from exceptions import BadRequestException
from data_processing.api.api import Api

class SetDaoApi(ISetDaoApi, Api):

    def __init__(self) -> None:
        super().__init__()

    # region : Operations
    def get_last_sets_by_player(self, idPlayer : int, page : int) -> [Set]:
        """
        Retourne les 10 sets d'un joueur en fonction d'une page.

        Args:
            idPlayer (int): L'id du joueur.
            page (int): La page à afficher.

        Returns:
            [Set]: Les sets.

        Raises:
            Exception: Si la requête échoue.
        """
        pass
        # Récupération des sets
        response = self.sg.request_api("""
                                        query SetsByPlayer($idPlayer : ID!, $page : Int!) {
                                                player(id: $idPlayer) {
                                                    sets(perPage: 10, page : $page) {
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
                        "idPlayer": idPlayer,
                        "page": page
                    })
        
        # Gestion des erreurs
        if "errors" in response:
            raise BadRequestException(response["errors"][0]["message"])
        
        # Ajout des sets à la liste
        sets = []
        if "data" in response:
            for data_set in response['data']['player']['sets']['nodes']:
                set = Set()
                set.hydrate(data_set)
                # Vérification que le set est terminé
                if set.WinnerId is not None:
                    sets.append(set)
        return sets
    
    # endregion