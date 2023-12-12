from model.event import Event
from abc import ABC, abstractmethod

class IEventDaoApi(ABC):

    @abstractmethod
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
        pass