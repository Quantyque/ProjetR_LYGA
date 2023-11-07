from model.event import Event
from manager.manager import Manager

class EventManager(Manager):
    """
    Classe permettant de gérer les événements
    """

    def __init__(self):
        super().__init__()

    # region Operations

    def get_event_by_id(self, id : int, page : int) -> Event:
        """
        Récupère un événement par son id

        Args:
            id (int): l'id de l'événement
            page (int): la page de l'événement

        Returns:
            Event: l'événement récupéré
        """
        event : Event = Event()
        response : dict = super().request_api("""
                    query EventById($idEvent: ID!, $page : Int!) {
                        event(id: $idEvent) {
                            id
                            name
                            numEntrants
                            tournament{
                                id
                                name
                            }
                            entrants(query : {perPage:500}){
                                nodes{
                                    standing{
                                        player{
                                            id
                                            prefix
                                            gamerTag
                                        }
                                    }
                                }
                            }
                            sets(page: $page, perPage: 50, sortType: RECENT) {
                            nodes {
                                id
                                round
                                winnerId
                                event{
                                id
                                name
                                }
                                slots {
                                entrant {
                                    id
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
                        "idEvent": id,
                        "page": page
                    })
        data_event : dict = response["data"]["event"]
        event.hydrate(data_event)
        return event
    
    #endregion

    

    