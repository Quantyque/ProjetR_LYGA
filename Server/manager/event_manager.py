from model.event import Event
from data_processing.api.startgg.event.IEventDaoApi import IEventDaoApi
from data_processing.api.startgg.event.EventDaoApi import EventDaoApi

class EventManager():
    """
    Classe permettant de gérer les événements
    """

    def __init__(self):
        self.__sg: IEventDaoApi = EventDaoApi()

    # region Operations

    def get_event_by_id(self, id : int, page : int) -> Event:
        """
        Récupère un événement par son id.

        Args:
            id (int): L'id de l'événement.
            page (int): La page de l'événement.

        Returns:
            Event: L'événement.

        Raises:
            HTTPError: Si la requête échoue.
        """
        return self.__sg.get_event_by_id(id, page)
    
    #endregion

    

    