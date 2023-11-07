from model.entity import Entity
from model.event import Event

class Tournament(Entity):
    """
    Représente un tournoi de jeu vidéo
    """
    def __init__(self):
        self.__id : int = None
        self.__name : str = None
        self.__owner : str = None
        self.__lat : float = None
        self.__lng : float = None
        self.__events : [Event] = []

    # region Properties
    @property
    def Id(self) -> int:
        """
        Id du tournoi
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        self.__id = id

    @property
    def Name(self):
        """
        Nom du tournoi
        """
        return self.__name
    
    @Name.setter
    def Name(self, name : str) -> None:
        self.__name = name

    @property
    def Owner(self):
        """
        Propriétaire du tournoi
        """
        return self.__owner
    
    @Owner.setter
    def Owner(self, owner : str) -> None:
        self.__owner = owner

    @property
    def Location(self):
        """
        Localisation du tournoi
        """
        return "(" + str(self.__lat) + "," + str(self.__lng) + ")"

    @property
    def Events(self):
        """
        Evenements aillant lieu dans le tournoi
        """
        return self.__events
    
    @Events.setter
    def Events(self, events : [Event]) -> None:
        self.__events = events

    # endregion

    # region Operations
    def hydrate(self, data):
        if "id" in data:
            self.Id = data["id"]
        if "name" in data:
            self.Name = data["name"]
        if "owner" in data:
            self.Owner = data["owner"]["name"]
        if "lat" in data:
            self.__lat = data["lat"]
        if "lng" in data:
            self.__lng = data["lng"]
        if "events" in data:
            for event in data["events"]:
                current_event = Event()
                current_event.hydrate(event)
                self.Events.append(current_event)

    def toJSON(self):
        json = {
            "id": self.Id,
            "name": self.Name,
            "owner": self.Owner,
            "location": self.Location,
            "events": [
                event.toJSON() for event in self.Events
            ]
        }
        return json
    # endregion