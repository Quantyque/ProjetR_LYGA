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
        Getter de l'id du tournoi

        Returns:
            int: Id du tournoi
        """
        return self.__id
    
    @Id.setter
    def Id(self, id : int) -> None:
        """
        Setter de l'id du tournoi

        Args:
            id (int): Nouvel id du tournoi
        """
        self.__id = id

    @property
    def Name(self):
        """
        Getter du nom du tournoi

        Returns:
            str: Nom du tournoi
        """
        return self.__name
    
    @Name.setter
    def Name(self, name : str) -> None:
        """
        Setter du nom du tournoi

        Args:
            name (str): Nouveau nom du tournoi
        """
        self.__name = name

    @property
    def Owner(self):
        """
        Getter du propriétaire du tournoi

        Returns:
            str: Propriétaire du tournoi
        """
        return self.__owner
    
    @Owner.setter
    def Owner(self, owner : str) -> None:
        """
        Setter du propriétaire du tournoi

        Args:
            owner (str): Nouveau propriétaire du tournoi
        """
        self.__owner = owner

    @property
    def Location(self):
        """
        Getter de la localisation du tournoi

        Returns:
            str: Localisation du tournoi
        """
        return "(" + str(self.__lat) + "," + str(self.__lng) + ")"

    @property
    def Events(self):
        """
        Getter des évenements aillant lieu dans le tournoi

        Returns:
            [Event]: Evenements aillant lieu dans le tournoi
        """
        return self.__events
    
    @Events.setter
    def Events(self, events : [Event]) -> None:
        """
        Setter des évenements aillant lieu dans le tournoi

        Args:
            events ([Event]): Nouveaux évenements aillant lieu dans le tournoi
        """
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