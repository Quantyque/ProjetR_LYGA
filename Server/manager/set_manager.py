from manager.manager import Manager
from model.set import Set

class SetManager(Manager):
    """
    Classe permettant de gérer les matchs
    """

    def __init__(self):
        super().__init__()

    # region Operations

    def get_last_sets_by_player(self, idPlayer : int) -> [Set]:
        """
        Renvoie la liste des derniers sets joués par un joueur
        """
        response = super().request_api("""
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
        sets = []
        if "data" in response:
            for data_set in response['data']['player']['sets']['nodes']:
                set = Set()
                set.hydrate(data_set)
                sets.append(set)
        return sets

    
    #endregion