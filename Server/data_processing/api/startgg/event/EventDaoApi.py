from data_processing.api.startgg.event.IEventDaoApi import IEventDaoApi
from model.event import Event
from exceptions import BadRequestException
from data_processing.api.api import Api

class EventDaoApi(IEventDaoApi, Api):
        
    def __init__(self):
        super().__init__()

    # region Operations

    def get_event_by_id(self, id : int, page : int) -> Event:
        """
        Réupère un évènement par son id.

        Args:
            id (int): L'id de l'évènement.
            page (int): La page.
        
        Returns:
            Event: L'évènement.
    
        Raises:
            Exception: Si la requête échoue.
        """
        event : Event = Event()
        response : dict = self.sg.request_api("""
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
        
        if "errors" in response and response["errors"]:
            raise BadRequestException(response["errors"][0]["message"])
        
        data_event : dict = response["data"]["event"]
        event.hydrate(data_event)
        return event
    
    # endregion